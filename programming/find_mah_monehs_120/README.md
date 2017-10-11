# GryphonCTF_2017: Find Mah Monehs

**Category:** Programming
**Points:** 120
**Description:**

>NEEDZ HALPZ ME 2 FIND MAH MONEHS 2 BUY SUM GAMEZ. ME WANTS $100. CAN HALP PLZ? THX M8!
`nc prog.chal.gryphonctf.com 17454`
_Creator - @Platy_

**Hint:**

>PATH FINDIN ALGORITHM M8

## Write-up
This challenge is by a certain mammal, mainly testing on the knowledge of pathfinding algorithms. However, as a wise old man once said to me, there's no reason to reinvent a perfectly in-shape Goodyear.

For this challenge, we will be using the [pathfinding library by @brean](https://github.com/brean/python-pathfinding).

    pip3 install git+https://github.com/brean/python-pathfinding

Using [Python](solve.py), we can solve this challenge really easily.

    # ./solve.py 
    [+] Opening connection to prog.chal.gryphonctf.com on port 17454: Done
    [+] Cracking RSA...: GCTF{1_w45_br0k3_bu7_n0_m0r3}
    [*] Closed connection to prog.chal.gryphonctf.com port 17454

Therefore, the flag is `GCTF{1_w45_br0k3_bu7_n0_m0r3}`.
