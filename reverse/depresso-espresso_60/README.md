# GryphonCTF_2017:

**Category:** Reverse
**Points:** 60
**Description:**

>I've intercepted a couple of files. I've been trying to work out how to use the program but it constantly gives me an error. I've drank countless cups of java, but I'm still stuck. Help me please!
_Creator - @Platy_

**Hint:**

>Feistel. Just Feistel.

## Write-up
This challenge touches upon Java reversing skills, as well as transpiling. We are given a `.zip` archive with a `Data.class`, `Flag.class` as well as an `output.bin` file. We can start with reversing both classes with a tool like [JD-GUI](http://jd.benow.ca/).

Firstly, rename the `.zip` file to `.jar` and open it in JD-GUI, we can then simply decompile each `.class` files to their pseudo-sources.

Firstly, for `Data.class`,

    import java.io.Serializable;
    import javax.crypto.SealedObject;
    import javax.crypto.SecretKey;

    public class Data
      implements Serializable
    {
      private final SealedObject sealed;
      private final SecretKey key;
      
      public Data(SealedObject paramSealedObject, SecretKey paramSecretKey)
      {
        this.sealed = paramSealedObject;
        this.key = paramSecretKey;
      }
      
      public SealedObject getSealed()
      {
        return this.sealed;
      }
      
      public SecretKey getKey()
      {
        return this.key;
      }
    }

and `Flag.class`,

    import java.io.Serializable;

    public class Flag
      implements Serializable
    {
      private final String flag;
      
      public Flag(String paramString)
      {
        this.flag = paramString;
      }
      
      public String getFlag()
      {
        return this.flag;
      }
    }

Not too hard, now all we have to do is load these classes up on another [Java](Solution.java) class and get our flag.

    $ javac Solve.java
    $ java Solve
    GCTF{d35_l0v35_4_6r347_c1ph3r}

Therefore, the flag is `GCTF{d35_l0v35_4_6r347_c1ph3r}`.
