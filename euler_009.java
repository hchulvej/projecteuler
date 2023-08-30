import java.util.Arrays;

public class euler_009 {

    public static void main(String[] args) {

        long startTime = System.nanoTime();

        int res = 0;

        for (int i = 1; i < 500; i++) {
            for (int j = i + 1; 1000 - i - j > 0; j++) {
                int k = 1000 - i - j;
                if (i * i + j * j == k * k) {
                    res = i * j * k;
                }
            }
        }

        long duration = System.nanoTime() - startTime;

        System.out.println("The product abc is " + res + ". Runtime took around " + duration
                + " nanoseconds.");
    }
}
