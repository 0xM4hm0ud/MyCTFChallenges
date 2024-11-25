# Space Maze

|||
|-|-|
|  **CTF**  |  [1337UP LIVE CTF 2024](https://ctf.intigriti.io/) [(CTFtime)](https://ctftime.org/event/2446)  |
|  **Author** |  0xM4hm0ud & et3rnos |
|  **Category** |  Game |
|  **Solves** | 3  |
|  **Difficulty** |  Medium/Hard |

<img src="https://github.com/user-attachments/assets/b82a2753-59d2-40fb-b37d-c80d67a1a15e" width="400">

# Solution

The goal of this challenge was to solve 100 mazes (later reduced to 50 due to server performance issues).
You needed to find a portal, and upon colliding with it, you would be teleported to a new maze.

The game was compiled with il2cpp. You could use MelonLoader to solve this challenge.
Frida was also a viable option. [Here](https://github.com/tien0246/writeup/tree/main/spacemaze) is a writeup from one of the solvers during the CTF with Frida.

# Files

To try the challenge locally, you can download the game and server from [this link](https://cybersharing.net/s/947ddbfdbed9d4dc).
The password to access the files is `spacemaze`. The game is configured with the IP address set to `127.0.0.1`.

The server runs on UDP port `6666`, and the client will attempt to connect to `127.0.0.1:6666` via UDP.
If you want to change the IP address, you can modify it in `\Fun With Spikes_Data\il2cpp_data\Metadata\globals.metadata` located in the game folder.
Ensure the new IP address is the same length as `127.0.0.1`. You can use a tool like sed to replace it.
