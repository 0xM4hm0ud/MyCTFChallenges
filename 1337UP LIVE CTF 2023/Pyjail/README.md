# Pyjail

|||
|-|-|
|  **CTF**  |  [1337UP LIVE CTF 2023](https://ctf.intigriti.io/) [(CTFtime)](https://ctftime.org/event/2134)  |
|  **Author** |  0xM4hm0ud |
|  **Category** |  Misc |
|  **Solves** |  87  |
|  **Difficulty** |  Easy |
| **Files** |  [jail.py](<jail.py>)  |

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/df7d3593-fa2a-469b-a818-84b7ef9a5ed9)

# Solution

We get an python file as attachment: 

```py
import ast
import unicodedata

blacklist = "0123456789[]\"\'._"
check = lambda x: any(w in blacklist for w in x)

def normalize_code(code):
    return unicodedata.normalize('NFKC', code)

def execute_code(code):
    try:
        normalized_code = normalize_code(code)
        parsed = ast.parse(code)
        for node in ast.walk(parsed):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    if node.func.id in ("os","system","eval","exec","input","open"):
                        return "Access denied!"
            elif isinstance(node, ast.Import):
                return "No imports for you!"
        if check(code):
            return "Hey, no hacking!"
        else:
            return exec(normalized_code, {}, {})
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    while True:
        user_code = input(">> ")
        if user_code.lower() == 'quit':
            break
        result = execute_code(user_code)
        print("Result:", result)
```

We can see that it takes our input. If `quit` is sent the program will exit otherwise it will call `execute_code` with out input.
In `execute_code` it first normalize our input with calling the function `normalize_code`:

 ```py
def normalize_code(code):
    return unicodedata.normalize('NFKC', code)
```

This will normalize unicode. So unicode bypass is not possible. The program then parse the code with [ast](https://docs.python.org/3/library/ast.html). It then walks through the tree and check if there is an function call or an import.
If there is a function call it checks if the function is in `("os","system","eval","exec","input","open")`. If it is it will not execute our code.

```py
       parsed = ast.parse(code)
        for node in ast.walk(parsed):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    if node.func.id in ("os","system","eval","exec","input","open"):
                        return "Access denied!"
            elif isinstance(node, ast.Import):
                return "No imports for you!"
```  

After this check it will call `check` with our input. `check` is:

```py
blacklist = "0123456789[]\"\'._"
check = lambda x: any(w in blacklist for w in x)
```

This checks if any char in our input is in blacklist. So numbers and `[]"'._` are not allowed.

After this it will execute our code with `exec`: `return exec(normalized_code, {}, {})`.
We can see that the globals(second param in exec) is an empty dictionary. The builtins are not removed, so we can use builtins function. We cant use import because we checked that with ast. 
My solution was to use breakpoint. This is an built in function in python:

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/6fced036-35b8-4f7d-9ba5-d95a4a67b872)

We then can use this inside our pdb shell to get the flag:

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/59803fda-021b-4566-bdae-2baecee114c6)

