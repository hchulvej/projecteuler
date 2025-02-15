import java.util.Arrays;

public class euler_003 {

    public static void main(String[] args) {

        long startTime = System.nanoTime();

        int upperBound = (int) Math.ceil(Math.sqrt((double) 600851475143L));

        int largestFactor = 1;

        boolean[] sieve = new boolean[upperBound + 1];
        Arrays.fill(sieve, true);

        for (int n = 3; n <= upperBound; n+=2) {
            if (sieve[n]) {
                int m = 2;
                while (m * n <= upperBound) {
                    sieve[m * n] = false;
                    m++;
                }
                if (600851475143L % n == 0) {
                    largestFactor = n;
                }
            }
        }

        long duration = System.nanoTime() - startTime;

        System.out.println("The largest prime factor is " + largestFactor + ". Runtime took around " + duration + " nanoseconds.");
    }
    
}
