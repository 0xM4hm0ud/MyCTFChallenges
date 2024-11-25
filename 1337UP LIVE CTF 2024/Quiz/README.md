# Quiz

|||
|-|-|
|  **CTF**  |  [1337UP LIVE CTF 2024](https://ctf.intigriti.io/) [(CTFtime)](https://ctftime.org/event/2446)  |
|  **Author** |  0xM4hm0ud |
|  **Category** |  Mobile |
|  **Solves** |  61  |
|  **Difficulty** |  Easy |

<img src="https://github.com/user-attachments/assets/74eb881f-3aa3-4e37-a814-232bbc46148c" width="400">

# Solution

```py
import requests
import json
import time

# Configurations
url = "https://localhost:8443"
start_endpoint = "/start"
submit_endpoint = "/submit"
headers = {
    "Content-Type": "application/json",
    "User-Agent": "okhttp/4.12.0"
}

# Disable SSL warnings for testing
requests.packages.urllib3.disable_warnings()

def solve_equation(equation):
    """Evaluates a simple equation in string format."""
    try:
        return eval(equation)
    except Exception as e:
        print(f"Error solving equation {equation}: {e}")
        return 0

def start_game():
    """Starts a game session and returns game details."""
    start_time = time.time()
    payload = {"start_time": start_time}
    try:
        response = requests.post(
            url + start_endpoint, headers=headers, json=payload, verify=False
        )
        if response.status_code == 200:
            data = response.json()
            game_id = data.get("game_id")
            equations = data.get("equations")
            print(f"Game started! Game ID: {game_id}")
            return game_id, equations, start_time
        else:
            print(f"Failed to start game: {response.status_code}")
            return None, None, None
    except Exception as e:
        print(f"Error in start_game: {e}")
        return None, None, None

def submit_game(game_id, total_sum, start_time):
    """Submits the game results."""
    end_time = str(total_sum + start_time)
    payload = {
        "game_id": game_id,
        "end_time": end_time
    }
    try:
        response = requests.post(
            url + submit_endpoint, headers=headers, json=payload, verify=False
        )
        if response.status_code == 200:
            result = response.json()
            print(f"Game result: {result}")
        else:
            print(f"Failed to submit game: {response.status_code}")
    except Exception as e:
        print(f"Error in submit_game: {e}")

def play_game():
    """Function to play a single game."""
    game_id, equations, start_time = start_game()
    if game_id and equations:
        total_sum = sum(solve_equation(eq) for eq in equations)
        submit_game(game_id, total_sum, start_time)

if __name__ == "__main__":
    play_game()
```


