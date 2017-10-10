#! /usr/bin/env python3
##
# Created for GryphonCTF 2017_50 Shades Of Pixels
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
from PIL import Image
from pwn import *

# Open file
im = Image.open("./flag-e89619f149a311e9e60b7107317217b7.png")
pix = im.load()
width, height = im.size

# Logging
with log.progress("Cracking ASCII...") as p:
    # Read flag from file
    flag = []
    for x in range(width):
        r, g, b = pix[x, 0]
        char = chr(r)
        flag.append(char)

        # Check if closing bracket, just asthetics
        if char == "}":
            break

    # Output flag
    p.success("".join(flag))
