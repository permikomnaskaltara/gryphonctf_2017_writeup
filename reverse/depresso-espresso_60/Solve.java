/**
 * Created for the GryphonCTF 2017_Depresso Espresso
 * By Amos (LFlare) Ng <amosng1@gmail.com>
 */
import java.io.*;
import javax.crypto.*;

public class Solve {
    public static void main(String[] args) {
        try {
            // Load binary file
            FileInputStream fis = new FileInputStream("output.bin");

            // Read data class from sealed object
            ObjectInputStream ois = new ObjectInputStream(fis);
            Data data = (Data)ois.readObject();

            // Get sealed object
            SealedObject sealedObject = data.getSealed();

            // Get secret key and prepare cipher
            SecretKey secretKey = data.getKey();
            Cipher cipher = Cipher.getInstance("DES/ECB/PKCS5Padding");
            cipher.init(Cipher.DECRYPT_MODE, secretKey);

            // Get flag
            Flag flag = (Flag)sealedObject.getObject(cipher);

            // Print flag
            System.out.println(flag.getFlag());
        } catch (Exception e) {}
    }
}
