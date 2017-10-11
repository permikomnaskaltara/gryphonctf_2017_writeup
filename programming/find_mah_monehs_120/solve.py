#! /usr/bin/env python3
##
# Created for GryphonCTF 2017_Find The Monehs
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
from collections import defaultdict
from pwn import *
import re

# Pathfinding
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

# Functions
def find_points(challenge):
    start = "@"
    end = "$"

    # Find starting point
    for y, row in enumerate(challenge):
        for x, cell in enumerate(row):
            if cell == start:
                start = (y, x)
            if cell == end:
                end = (y, x)

    # Return points
    return start, end

def find_path(challenge, start, end):
    # Convert paths appropriately
    for y in range(len(challenge)):
        for x in range(len(challenge[y])):
            if challenge[y][x] == "-":
                challenge[y][x] = 1
            else:
                challenge[y][x] = 0

    # Use library to find our path
    grid = Grid(matrix=challenge)
    start = grid.node(start[1], start[0])
    end = grid.node(end[1], end[0])
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path_nodes, _ = finder.find_path(start, end, grid)

    # Convert path to wasd
    previous = None
    path = ""
    for step in path_nodes:
        if previous is not None:
            if step[1] < previous[1]:
                path += "w"
            if step[0] < previous[0]:
                path += "a"
            if step[1] > previous[1]:
                path += "s"
            if step[0] > previous[0]:
                path += "d"
        previous = step

    # Return path
    return path

# Create tube
t = remote("prog.chal.gryphonctf.com", 17454)

# Logging
with log.progress("Cracking RSA...") as p:

    # Receive header and send <enter>
    t.recvuntil("PRES ENTR 2 START!\n")
    t.sendline("")

    for i in range(99999):
        # Get rid of header
        header = b"\n".join(t.recvlines(2)).decode()
        if "FLAG" in header:
            flag = t.recvline().decode()
            p.success(flag)
            break

        # Get challenge and remove formatting
        challenge = t.recvuntil("\n\n").decode()
        challenge = re.sub("[^+\-@$\n\s]", "", challenge)

        # Split challenge up into arrays
        challenge = challenge.strip().split("\n")
        challenge = [row.strip().split("  ") for row in challenge]

        # Get points
        start, end = find_points(challenge)

        # Replace start and end with walkable points
        challenge[start[0]][start[1]] = "+"
        challenge[end[0]][end[1]] = "+"

        # Find path
        path = find_path(challenge, start, end)

        # Update progress
        p.status(f"Round {i}, Start: {start}, End: {end}, Path: {path}")

        # Send path
        t.sendline(path)
