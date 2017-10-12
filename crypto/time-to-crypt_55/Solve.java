package Time_to_Crypt;

import java.io.*;
import java.util.*;
import Time_to_Crypt.OTP.Data;

public class Solve {
    public static byte[] otp_gen() {
        Random randomno = new Random();
        byte[] nbyte = new byte[30];
        randomno.nextBytes(nbyte);
        return nbyte;
    }

    public static byte[] encrypt(byte[] data, byte[] key) {
        byte[] encrypted = new byte[data.length];
        for (int i = 0; i < data.length; i++) {
            encrypted[i] = (byte) (data[i] ^ key[i % key.length]);
        }
        return encrypted;
    }

    public static void main(String[] args) throws Exception {
        // Open file input stream
        FileInputStream fis = new FileInputStream("output");

        // Read data class from sealed object
        ObjectInputStream ois = new ObjectInputStream(fis);
        Data data = (Data)ois.readObject();

        // Get OTP
        byte[] data1 = "Congratulations! Here is the flag!".getBytes();
        byte[] otp = encrypt(data.getData1(), data1);

        // Decrypt
        byte[] data2 = encrypt(data.getData2(), otp);

        // Get as string
        String flag = new String(data2);

        // Print
        System.out.println(flag);
    }
}
