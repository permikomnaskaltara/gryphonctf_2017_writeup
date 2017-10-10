# GryphonCTF_2017: 50 Shades Brighter

**Category:** Forensics
**Points:** 80
**Description:**

>Alice - "Wow, this is just too dark!"
Bob - "Fine! I'll make it brighter!"
`[Update] 08/10/2017 07:20PM - Hint 1 released`
_Creator - @LFlare_

**Hint:**

>It's now twice the brightness, twice the fun!

## Write-up
Solution to this challenge can be done in many ways, though my personal recommendation is through Python's `PIL` library. Additionally, this challenge is built off the previous challenge, 50 Shades of Pixels.

With the only clue word, "brighter", participants are expected to think logically and play with brightness settings on the image, except the correct answer is to bitshift it. This is also easily accomplished in [Python](solve.py) and using the Pillow library.

    # ./solve.py 
    [+] Cracking UTF-8...: GCTF{n0w_7h3y_4r3_ju57_2_h4w7_2_br16h7_4_m3}

Therefore, the flag is `GCTF{n0w_7h3y_4r3_ju57_2_h4w7_2_br16h7_4_m3}`.
