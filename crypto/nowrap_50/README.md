# GryphonCTF_2017: NoWrap

**Category:** Crypto
**Points:** 50
**Description:**

>My white candy wrapper had this weird numbers encoded in it's molecular structure, I think it might contain the full recipe of the candy, can you help me get to the bottom of it?
_Creator - @LFlare_

**Hint:**

>n = pq, m = ?, c = ?

# NoWrap
The solution to this is simple. From the RSA algorithms, the challenge is simply exploiting the length problem of RSA.

    `c = m ** e mod n`

Where the modulo of `n` gives the ciphertext the irreversibility. However, that's only possible if `m` to the power of `e` is greater than `n`. Since we have a small `m` and an even smaller `e`, we don't ever exceed `n`.

So, to solve this, simply take `m` and `e`-root it. This can be done using `gmpy2` in Python and using [another script](solve.py).

    # ./solve.py 
    [+] Cracking Factorials...: GCTF{7h3_m355463_15_h1l4r10u5ly_5h0r7}

Therefore, the flag is `GCTF{7h3_m355463_15_h1l4r10u5ly_5h0r7}`.
