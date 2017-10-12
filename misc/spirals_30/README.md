# GryphonCTF_2017: Spirals

**Category:** Misc
**Points:** 30
**Description:**

>I just read junji ito's uzumaki and i am very inspired, so i decided to implement a simple obfuscation function! heres the link to the comic:
https://goo.gl/zur32R
Good luck!
_Creator - @paux_

## Write-up
This challenge involves reading the challenge title, realizing the file given is a barcode and programming up something that loops our characters in a literal _spiral_.

For this particular challenge, I'll be making use of the `pillow` and `zbarlight` libraries to automate the QR retrieving process as well as a [custom-coded spiralizer](solve.py).

    # ./solve.py 
    [+] Cracking Mona Lisa...: 
        █▀▀▀▀▀█ ▀▄█▄█ █   █▀▀▀▀▀█
        █ ███ █ ███ ▄██▄█ █ ███ █
        █ ▀▀▀ █ ▀ ▄█▀  ▀▀ █ ▀▀▀ █
        ▀▀▀▀▀▀▀ ▀ █ █ █ █ ▀▀▀▀▀▀▀
        █▀▀█▄▄▀ █ █▀█ ▄  █  ▀▀▀▄█
        ▄▄ █▄▄▀  ██▀▀▄ ▄▀█ ▄▄▄▄▄▄
         ▀▀▀▀ ▀▀ █▀▄█▀  █▀▀▄██ ▄▀
        ▄▀  ▀█▀▀█▄▀█ ▀▄ ▄█▀██  █ 
          ▀▀▀ ▀▀█ █ ▀██▀█▀▀▀█▀▀  
        █▀▀▀▀▀█  ▄ ▄  ▀▄█ ▀ █▄▀▀█
        █ ███ █ ▄█   ▄█ █▀█▀█▄▄█▄
        █ ▀▀▀ █ █ ▀▄▄▄▄█  ▀▀▀▄█▀ 
        ▀▀▀▀▀▀▀ ▀▀ ▀▀  ▀ ▀▀▀  ▀▀▀
        GCTF{junj1_17o_5p1r415}

Therefore, the flag is `GCTF{junj1_17o_5p1r415}`.
