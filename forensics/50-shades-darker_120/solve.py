#! /usr/bin/env python3
##
# Created for GryphonCTF 2017_50 Shades Darker
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
from PIL import Image
from pwn import *

# Open file
im = Image.open("./flag-15c8d37a1d7799188d24039dd13b72a2.png")
pix = im.load()
width, height = im.size

# Logging
with log.progress("Cracking 日本語...") as p:
    # Read flag from file
    flag = []
    for x in range(width):
        r, g, b = pix[x, 0]
        char = chr((((r << 1) & 255) | (r >> 7) & 255))
        flag.append(char)

        # Check if closing bracket, just asthetics
        if char == "}":
            break

    # Output flag
    p.success("".join(flag))
