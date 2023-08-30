import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Arrays;

public class euler_008 {

    private static BufferedInputStream bis = null;
    private static String path = "C:\\test\\projecteuler\\euler_008.txt";
    private static byte[] digits = new byte[1000];

    public static void main(String[] args) {

        try {
            bis = new BufferedInputStream(new FileInputStream(path));
            bis.read(digits);
        } catch (IOException e) {
            e.printStackTrace();
        }

        StringBuffer sb = new StringBuffer();

        for (byte b : digits) {
            sb.append((char) b);
        }
        sb.trimToSize();

        String inputAsString = sb.toString();

        for (int j = 0; j + 13 < inputAsString.length(); j++) {
            String subString = inputAsString.substring(j, j + 13);
            System.out.println(Double.parseDouble(subString));
        }
    }
}
