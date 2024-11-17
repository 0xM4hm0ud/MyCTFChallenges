# Notepad 2

|||
|-|-|
|  **CTF**  |  [1337UP LIVE CTF 2024](https://ctf.intigriti.io/) [(CTFtime)](https://ctftime.org/event/2446)  |
|  **Author** |  0xM4hm0ud |
|  **Category** |  Pwn |
|  **Solves** | 48 |
|  **Difficulty** |  Medium |

![image](https://github.com/user-attachments/assets/32515c4c-58ce-4660-bd8f-2fc5923f8d70)

# Solution

Format string on the heap. GOT is writable. Overwrite free to system to get a shell. 

[solve.py](solve.py)
