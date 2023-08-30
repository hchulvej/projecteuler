import java.io.FileInputStream;
import java.io.IOException;

public class euler_008 {

    private static Scanner sc;
    private static String path = "C:\\test\\projecteuler\\euler_008.txt";
    private static String input = "";

    public static long product(String s) {
        String[] ls = s.split("");

        long prod = 1;
        for (String str : ls) {
            prod *= Long.parseLong(str);
        }
        return prod;
    }

    public static void main(String[] args) {

        long startTime = System.nanoTime();

        try {
            sc = new Scanner(new FileInputStream(path));
            while (sc.hasNextLine()) {
                input += sc.nextLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        String[] nonZeroParts = input.split("0");

        long greatestProduct = 0;

        for (String nzp : nonZeroParts) {
            if (nzp.length() > 12) {
                int offset = 0;
                while (offset + 12 < nzp.length()) {
                    String c = nzp.substring(offset, offset + 13);
                    long p = product(c);
                    if (p > greatestProduct) {
                        greatestProduct = p;
                    }
                    offset++;
                }
            }
        }

        long duration = System.nanoTime() - startTime;

        System.out.println("The greatest product is " + greatestProduct + ". Runtime took around " + duration
                + " nanoseconds.");
    }
}
