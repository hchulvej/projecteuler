import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;

public class euler_011 {

    private static BufferedInputStream bis = null;
    private static BufferedReader br = null;
    private static String path = "C:\\test\\projecteuler\\euler_011.txt";
    private static int[][] grid = new int[20][20];
    private static StringBuffer input = new StringBuffer();

    private static void parseInput(String str) {
        String[] arr = str.trim().split(" ");
        for (int i = 0; i < arr.length; i++) {
            int v = Integer.parseInt(arr[i]);
            grid[i / 20][i % 20] = v;
        }
    }

    public static void main(String[] args) {

        long startTime = System.nanoTime();

        try {
            bis = new BufferedInputStream(new FileInputStream(new File(path)));
            br = new BufferedReader(new InputStreamReader(bis, StandardCharsets.UTF_8));

            while (br.ready()) {
                input.append(br.readLine());
                input.append(" ");
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                bis.close();
                br.close();
            } catch (Exception e) {
                e.printStackTrace();
            }

        }

        parseInput(input.toString());

        int largestProduct = -1;

        for (int row = 0; row < 20; row++) {
            for (int col = 0; col < 20; col++) {
                // Right

                // Left

                //
            }
        }

        long duration = System.nanoTime() - startTime;

        System.out.println("The threatest product is " + largestProduct + ". Runtime took around " + duration
                + " nanoseconds.");
    }
}
