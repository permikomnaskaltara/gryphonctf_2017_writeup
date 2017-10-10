# GryphonCTF_2017: 50 Shades Of Pixels

**Category:** Forensics
**Points:** 40
**Description:**

>Bob - "I don't do plaintext."
Bob - "My methods of communication are unconventional."
Alice - "So show me?"
Bob - "Okay!"
`[Update] 07/10/2017 07:00PM - Hint 1 released`
`[Update] 08/10/2017 07:20PM - Hint 2 released`
_Creator - @LFlare_

**Hint:**

>Perhaps the colours mean something?
>R = G = B = ?

## Write-up
Solution to this challenge can be done in many ways, though my personal recommendation is through Python's `PIL` library.

Initially, receiving the file might give some people headaches wondering how I hid the message. Well, the very interesting pattern of shades of grey pixels might give you a hint. The message is encoded in the red, blue and green values of the pixels.

Reading the pixels from top left to top right will grant you the message, it's really easily solved in [Python](solve.py). You might need to install `pip` and run `pip install pillow` to get the neccessary libraries for this to work.

    # ./solve.py 
    [+] Cracking ASCII...: GCTF{p1x3l1z3d_53cr375_4r3_h4w7}

Therefore, the flag is `GCTF{p1x3l1z3d_53cr375_4r3_h4w7}`.
