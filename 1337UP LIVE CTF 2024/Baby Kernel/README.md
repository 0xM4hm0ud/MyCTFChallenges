# Baby Kernel

|||
|-|-|
|  **CTF**  |  [1337UP LIVE CTF 2024](https://ctf.intigriti.io/) [(CTFtime)](https://ctftime.org/event/2446)  |
|  **Author** |  0xM4hm0ud |
|  **Category** |  Pwn |
|  **Solves** | 40 |
|  **Difficulty** |  Easy |

![image](https://github.com/user-attachments/assets/ce21dbdc-b36f-4583-a755-ed0cf6bdcc7d)

# Solution

There is a stack overflow vulnerability. All protections are disabled except KASLR. 
I used commit_creds to get root. 

[exploit.c](exploit.c)
