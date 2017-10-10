#! /usr/bin/env python3
##
# Created for the Insanity challenge
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
from base64 import *
from pwn import *
import sys

# Logging
with log.progress("Cracking MD5...") as p:
    # Read flag from file
    with open("./fe3c84aa840d950f7f3d006ebc4db48f.txt") as file:
        flag = file.read().strip().encode()

    # Repeatedly decode flag
    while True:
        # Check if GCTF{ in flag
        if b"GCTF" in flag:
            p.success(flag.decode())
            break

        # Check if base16, base32, or base64
        try:
            attempt = b16decode(flag)
        except:
            try:
                attempt = b32decode(flag)
            except:
                try:
                    attempt = b64decode(flag)
                except:
                    quit("Invalid input?")

        # Set flag to attempt
        flag = attempt
