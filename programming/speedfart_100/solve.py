#! /usr/bin/env python3
##
# Created for GryphonCTF 2017_SpeedFart
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
from pwn import *
import re
import sys

# VARIABLES
REGISTERS = 16

# Functions
def solve(challenge):
    # Initialize
    registers = [0] * REGISTERS
    pointer = 0
    index = 0
    loops = 0
    recursions = []

    # Loop through challenges till end
    while index < len(challenge):
        # Get current symbol
        symbol = challenge[index]

        # If standard operations
        if symbol == ">":
            pointer += 1
        elif symbol == "<":
            pointer -= 1
        elif symbol == "+":
            registers[pointer] += 1
        elif symbol == "-":
            registers[pointer] -= 1

        # Check pointer sanity
        if pointer < 0 or pointer > REGISTERS:
            raise Exception("Pointer out of bounds!")

        # Iterate index
        index += 1

        # Wrap around register
        if registers[pointer] < 0:
            registers[pointer] = 255
        elif registers[pointer] > 255:
            registers[pointer] = 0

        # If loop operations
        if symbol == "[":
            # If register at pointer == 0
            if registers[pointer] == 0:
                # Go to end of loop
                depth = 1
                while depth > 0:
                    symbol = challenge[index]
                    if symbol == "[":
                        depth += 1
                    elif symbol == "]":
                        depth -= 1
                    index += 1  
            else:
                # Append to recursions
                recursions.append(index)
        elif symbol == "]":
            # If value at pointer is not 0, loop again
            if registers[pointer] != 0:
                loops += 1
                index = recursions.pop() - 1

            # Check if we are looping too much
            if loops > 100:
                raise Exception("Too many loops!")

    # Check that registers are non-empty
    for register in registers:
        if register != 0:
            return registers

    # If registers empty, raise exception
    raise Exception("Registers empty!")

# Create tube
t = remote("prog.chal.gryphonctf.com", 17455)

# Reply with readiness
t.recvuntil("[y/n] ")
t.sendline("y")

# Crack the code
with log.progress("Cracking DES...") as p:
    # While looping
    while True:
        # Get round header
        header = t.recvline().decode().strip()

        # Check if flag given
        if "GCTF" in header:
            p.success(header)
            quit()

        # Get round
        current_round = int(re.findall("[0-9]+", t.recvuntil("FIGHT!\n").decode())[0])
        p.status(f"Round {current_round}")

        # Prepare to receive challenge
        t.recvuntil("+-+-+-+-+-+-+-+-+-+-\n\n")

        # Receive challenge and solve
        challenge = list(t.recvuntil("\n\n").decode()[:-2])
        index = int(re.findall("[0-9]+", t.recvuntil("er? ").decode())[0])
        solution = str(solve(challenge)[index-1])

        # Send answer
        t.sendline(solution)

        # Receive "Correct!"
        t.recvline()
