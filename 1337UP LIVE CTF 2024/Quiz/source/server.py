from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
from time import time
import uuid
from secret import flag
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["5 per minute"]
)

class Game(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    equations = db.Column(db.Text, nullable=False)
    start_time = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

def generate_equations(amount):
    equations = []
    for _ in range(amount):
        operator_index = random.randint(0, 3)
        if operator_index == 0:
            a = random.randint(1, 2000)
            b = random.randint(1, 2000)
            equation = f"{a} + {b}"
        elif operator_index == 1:
            a = random.randint(1, 2000)
            b = random.randint(1, 2000)
            if a < b:
                a, b = b, a
            equation = f"{a} - {b}"
        elif operator_index == 2:
            a = random.randint(1, 300)
            b = random.randint(1, 300)
            equation = f"{a} * {b}"
        else:
            b = random.randint(2, 19)
            a = b * random.randint(1, 10)
            equation = f"{a} / {b}"
        equations.append(equation)
    return equations

@app.route('/start', methods=['POST'])
@limiter.limit("5 per minute")
def start_game():
    if request.user_agent.string != "okhttp/4.12.0":
        return '', 403

    client_time = request.json.get("start_time")

    if not client_time:
        return jsonify({"error": "Start time is required"}), 400

    while True:
        game_id = str(uuid.uuid4())
        existing_game = db.session.get(Game, game_id)
        if not existing_game:
            break

    equations = generate_equations(500)
    
    game = Game(
        id=game_id,
        equations=";".join(equations),
        start_time=float(client_time)
    )
    db.session.add(game)
    db.session.commit()

    return jsonify({"game_id": game_id, "equations": equations})

@app.route('/submit', methods=['POST'])
@limiter.limit("5 per minute")
def submit_game():
    if request.user_agent.string != "okhttp/4.12.0":
        return '', 403

    data = request.get_json()
    game_id = data.get("game_id")
    client_time = data.get("end_time")

    if not game_id or not client_time:
        return jsonify({"error": "Game ID and end time are required"}), 400

    game = db.session.get(Game, game_id)
    if not game:
        return jsonify({"error": "Invalid game ID"}), 400

    server_start_time = game.start_time
    current_server_time = time()
    server_allowed_time = server_start_time + 60

    equations = game.equations.split(";")
    
    total_sum = 0
    for equation in equations:
        try:
            total_sum += eval(equation)
        except Exception as e:
            return jsonify({"error": f"Failed to evaluate equation: {equation}"}), 400

    expected_end_time = server_start_time + total_sum

    if current_server_time > server_allowed_time:
        return jsonify({"result": "Time exceeded. Try again!"})

    if float(client_time) == expected_end_time:
        return jsonify({"result": flag})
    else:
        return jsonify({"result": "Incorrect end time. Try again!"})

@app.route('/health')
@limiter.limit("5 per minute")
def health_check():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
