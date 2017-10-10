#! /usr/bin/env python3
##
# Created for GryphonCTF 2017_50 Shades Brighter
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
from PIL import Image
from pwn import *

# Open file
im = Image.open("./flag-55103fd3f7615102bef82539018477b2.png")
pix = im.load()
width, height = im.size

# Logging
with log.progress("Cracking UTF-8...") as p:
    # Read flag from file
    flag = []
    for x in range(width):
        r, g, b = pix[x, 0]
        char = chr(r >> 1)
        flag.append(char)

        # Check if closing bracket, just asthetics
        if char == "}":
            break

    # Output flag
    p.success("".join(flag))
