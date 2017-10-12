# GryphonCTF_2017: Time To Crypt

**Category:** Crypto
**Points:** 55
**Description:**

>Alice has just learnt about encryption and OTPs in Applied Cryptography. Now she wants to put her knowledge to the test. She successfully implemented OTPs into her Java code, but the lecturer said that it is insecure.
_Creator - @Platy_

**Hint:**

>She did not fully understand that 'OT' in 'OTP' stands for 'One-Time'

## Write-up
This challenge is fairly straightforward, exploiting the unique property of the `XOR` operator to recover the `OTP` values to get the flag. As this challenge is done in Java, I have to also use Java to recover the flags.

    String flag = "GCTF{XXXXXXXXXXXXXXXXXXXXXXXXXXXX}"; // Flag goes here!
    String text = "Congratulations! Here is the flag!";
        
For the most part, the two lines we have to look at is.
        
    byte[] data1 = encrypt(text.getBytes(), otp);
    byte[] data2 = encrypt(flag.getBytes(), otp);

Part of the trick to solving this challenge is to realize that if we have the known plaintext and known ciphertext, we can reverse the xor key to use to decrypt the flag.

So, for starters, let's try to decrypt data1 with the known plaintext!

    // Get OTP
    byte[] data1 = "Congratulations! Here is the flag!".getBytes();
    byte[] otp = encrypt(data.getData1(), data1);

Now that we have the otp key, we can decrypt data2 to get our file. The final [code](Solve.java) helps us with this.

    # javac OTP.java Solve.java -d .
    # java Time_to_Crypt.Solve
    GCTF{p4ds_u53d_0n3_700_m4ny_71m35}

Therefore, the flag is `GCTF{p4ds_u53d_0n3_700_m4ny_71m35}`.
