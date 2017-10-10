# GryphonCTF_2017: SpeedFart

**Category:** Pwn
**Points:** 100
**Description:**

>This was originally written on a stone slab somewhere in a forest. I took it, tweaked it and served it.
`nc prog.chal.gryphonctf.com 17455`
_Creator - @LFlare_

## Write-up
This challenge is a mockup of @nnamon's challenge [A Forest](https://github.com/DISMGryphons/GryphonCTF2016-Challenges/tree/master/challs/programming/forest) where the objective is to solve code given in a limited amount of time. However, instead of assembly, the esoteric language [Brainf*ck](https://en.wikipedia.org/wiki/Brainfuck) is given instead.

Connecting to the server gives us,

    #!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#

    Hello there! I am the new automated testing machine!
    Unfortunately, I am also slightly stupid.

    I will ask you a series of questions.
    All you have to do, is send me your replies.
    The catch? You have to do it within 10 seconds.

    This may or may not help you:
    - 16 8-bit registers
    - 50.0 rounds

    Are you ready? [y/n] y

    ROUND 1, FIGHT!
    +-+-+-+-+-+-+-+-+-+-

    --+-->[-[+>-+->-<<>+->[<->-<-<[[>+<<>>---<<>+<+>]-<><+-><]><+[--
    ]]]]

    +-+-+-+-+-+-+-+-+-+-
    What value is in the 1st register? 

We are told that there are 16 registers and 50 rounds of code. This is in relation to something like this [visualizer](https://fatiherikli.github.io/brainfuck-visualizer/) page.

Well, how do you solve this? Using [Python](solve.py) of course!

    # ./solve.py 
    [+] Opening connection to prog.chal.gryphonctf.com on port 17455: Done
    [+] Cracking DES...: Flag is: GCTF{1_h0p3_y0u_d1d_n07_7ry_7h15_m4nu4lly}
    [*] Closed connection to prog.chal.gryphonctf.com port 17455

Therefore, the flag is `GCTF{1_h0p3_y0u_d1d_n07_7ry_7h15_m4nu4lly}`.
