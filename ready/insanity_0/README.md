# GryphonCTF_2017: Insanity

**Category:** Are You Ready?
**Points:** 0
**Description:**

>My bassist wrote this down on a piece of paper before he died of lack of Vitamin B, I'm going insane trying to figure out what he meant, can you help me?
_Creator - @LFlare_

## Write-up
Originally designed with an additional base in mind, it has since been removed due to stability. The solution for this challenge is to simply decode the flag over and over again. The only trick is with the usage of multiple bases, namely 16, 32 and 64. As such, we have to attempt to decode the flag in each bases in a nested try-except. This can be made a much easier task by writing a [script](solve.py).

    # ./solve.py 
    Flag: GCTF{b4535_4r3_c0nfu51n6_m4n}

Therefore, the flag is `GCTF{b4535_4r3_c0nfu51n6_m4n}`.
