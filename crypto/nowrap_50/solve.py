#! /usr/bin/env python3
##
# Created for GryphonCTF 2017_NoWrap challenge
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
from pwn import *
import gmpy2
import binascii

# Set precision
gmpy2.get_context().precision=1000

# Load flag file
exec(open("./flag-0fd9e17d87d7a4d42327c61c2295c2c4.txt").read())

# Logging
with log.progress("Cracking Factorials...") as p:
    # Cube root our message
    m = int(gmpy2.root(c, e))
    m = binascii.unhexlify(hex(m)[2:])
    m = m.decode()

    # Print message
    p.success(m[27:])
