import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Arrays;

public class euler_008 {
    
    private static BufferedInputStream bis = null;
    private static String path = "C:\\Java\\projecteuler\\euler_008.txt";

    public static void main(String[] args) {
        
        try {
            bis = new BufferedInputStream(new FileInputStream(path));
            System.out.println(Arrays.toString(bis.readNBytes(32)));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
