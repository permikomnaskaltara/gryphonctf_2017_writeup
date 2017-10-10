# GryphonCTF_2017: NoobPwn

**Category:** Pwn
**Points:** 30
**Description:**

>Getting tired of pwn? How about an easier one?
`nc pwn2.chal.gryphonctf.com 17346`
_Creator - @LFlare_

## Write-up
We are given two files, [noobpwn-a927b91937e19b93cb50f4a96ad82667.c](noobpwn-a927b91937e19b93cb50f4a96ad82667.c) and [noobpwn-redacted-564e969dbbe6bbd0da1c3e1064b379a5](noobpwn-redacted-564e969dbbe6bbd0da1c3e1064b379a5). Analyzing the files given to us, we come across quite a few interesting tidbits,

From the looks of it, we need to reach here,

    // Check if we have a winner
    if (!strcmp("GIMMEDAFLAG\n", buf)) {
        system("/bin/cat flag.txt");
        exit(0);
    }

Which means our `buf` needs to match `GIMMEDAFLAG\n`. However, how do we even get there? Well, it's as simple as these two lines.

    int fd = key - 0x31337;
    int len = read(fd, buf, 32);

In C, `stdin` or `standard input` is commonly denoted as `0`, so the secret key we have to provide must be able to be subtracted by `0x31337` to get `0`, so `0x31337` is our secret key.

Now, we just have to [script](solve.py) it all together (or do it manually),

    # ./solve.py 
    [+] Cracking Tic-Tac-Toe...: `GCTF{f1l3_d35cr1p70r5_4r3_n457y}`
    [+] Opening connection to pwn2.chal.gryphonctf.com on port 17346: Done
    [*] Closed connection to pwn2.chal.gryphonctf.com port 17346

Therefore, the flag is `GCTF{f1l3_d35cr1p70r5_4r3_n457y}`.
