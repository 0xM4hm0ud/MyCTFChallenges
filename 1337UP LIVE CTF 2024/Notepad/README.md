# Notepad

|||
|-|-|
|  **CTF**  |  [1337UP LIVE CTF 2024](https://ctf.intigriti.io/) [(CTFtime)](https://ctftime.org/event/2446)  |
|  **Author** |  0xM4hm0ud |
|  **Category** |  Pwn |
|  **Solves** | 78 |
|  **Difficulty** |  Easy |

<img src="https://github.com/user-attachments/assets/eb044610-c8cf-4ce9-9f37-37e418da80df" width="400">

# Solution

Use the house of force technique to overwrite the top chunk.

Calculate the offset to `key`. Get a chunk at key and overwrite it with `0xcafebabe` to get the flag.

[solve.py](solve.py)
