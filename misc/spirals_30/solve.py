#! /usr/bin/env python3
##
# Created for GryphonCTF 2017_Spirals
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
from collections import defaultdict
from PIL import Image, ImageDraw, ImageFont
from pwn import *
import re
import time
import zbarlight

# Logging
with log.progress("Cracking Mona Lisa...") as p:
    # Open file
    with open("spiral_a25bd666a8832dad8c5ba86f840605f5.txt", "r",
              encoding="utf-16") as file:
        spirals = file.read().strip()

    # Size
    max_y = 13
    max_x = 25

    # Create matrix
    matrix = [[" " for x in range(max_x)] for y in range(max_y)]

    # Loop through characters
    y = 0
    x = 0
    counter = 0
    direction = 0
    turns = 0
    # for c in range(80):
    for c in spirals:
        # Set matrix cell
        matrix[y][x] = c

        # Iterate counter
        counter += 1

        # Calculate direction
        if direction == 0:
            if counter >= max_x:
                direction = 1
                counter = 1
                turns += 1
                y += 1

                if turns >= 3:
                    max_y -= 1
            else:
                x += 1
        elif direction == 1:
            if counter >= max_y:
                direction = 2
                counter = 1
                turns += 1
                x -= 1

                if turns >= 3:
                    max_x -= 1
            else:
                y += 1
        elif direction == 2:
            if counter >= max_x:
                direction = 3
                counter = 1
                turns += 1
                y -= 1

                if turns >= 3:
                    max_y -= 1
            else:
                x -= 1
        elif direction == 3:
            if counter >= max_y:
                direction = 0
                counter = 1
                turns += 1
                x += 1

                if turns >= 3:
                    max_x -= 1
            else:
                y -= 1

        # Format matrix
        fmt_matrix = ("\n".join([
            "".join([
                str(item) for item in line])
            for line in matrix]))

        # Replace matrix
        fmt_matrix = re.sub(r"¦", "█", fmt_matrix)
        fmt_matrix = re.sub(r"¯", "▀", fmt_matrix)
        fmt_matrix = re.sub(r"_", "▄", fmt_matrix)

        # Print matrix
        p.status(f"\n{fmt_matrix}")

        # Sleep
        time.sleep(0.001)

    # Prepare image and font
    W, H = (200, 200)
    font = ImageFont.truetype("andale-mono.ttf", size=10)
    im = Image.new('RGB', (W, H), (255, 255, 255))

    # Prepare to draw text in
    draw = ImageDraw.Draw(im)
    w, h = draw.multiline_textsize(fmt_matrix, font=font, spacing=0)

    # Draw QR code
    draw.multiline_text(((W-w)/2, (H-h)/2), fmt_matrix, font=font, fill=(0, 0, 0), spacing=0)

    # Scan image for QR codes
    flag = zbarlight.scan_codes('qrcode', im)[0].decode()

    # Success!
    p.success(f"\n{fmt_matrix}\n{flag}")
