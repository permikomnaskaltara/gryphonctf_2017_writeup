# GryphonCTF_2017: PseudoShell

**Category:** Pwn
**Points:** 60
**Description:**

>I managed to hook on to a shady agency's server, can you help me secure it?
`nc pwn2.chal.gryphonctf.com 17341`
_Creator - @LFlare_

## Write-up
**_Disclaimer: This challenge was originally meant to be harder, but I broke it, so now everyone thinks pwn is easy._**

Aprils' Fool! It's not actually CIA servers. Disclaimer, `// Add one more to fgets for null byte` is not a real thing, you should always use the exact size minus 1 when using `fgets`.

For this challenge, it tests on the concept of stack following the structure of the code. Particularly, we want to focus on the `login()` function, with the variables `access` and `password`. When compiled, this is how they would behave like.

    [ PASSWORD - 16 bytes ]
    [ ACCESS - 4 byte ]

As you see, by writing 17 bytes, you would be enroaching onto the `access` variable. By simply overwriting that byte containing the initial `0xff`, you easily break the system.

Like always, a [Python](solve.py) for it all.

    # ./solve.py 
    [+] Cracking WEP...: GCTF{0ff_by_0n3_r34lly_5uck5}
    [+] Opening connection to pwn2.chal.gryphonctf.com on port 17341: Done
    [*] Closed connection to pwn2.chal.gryphonctf.com port 17341

Therefore, the flag is `GCTF{0ff_by_0n3_r34lly_5uck5}`.
