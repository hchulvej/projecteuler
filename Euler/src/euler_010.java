import java.math.BigInteger;
import java.util.Arrays;

public class euler_010 {

    private static boolean[] primes = new boolean[2000000];
    private static BigInteger sum = BigInteger.ZERO;


    public static void main(String[] args) {

        long startTime = System.nanoTime();
        
        Arrays.fill(primes, true);
        primes[0] = false;
        primes[1] = false;
        for (int i = 2; i < primes.length; i++) {
            if (primes[i]) {
                sum = sum.add(new BigInteger("" + i));
                int m = 2;
                while (m * i < primes.length) {
                    primes[m * i] = false;
                    m++;
                }
            }
        }

        long duration = System.nanoTime() - startTime;
        
        System.out.println("The sum of primes is " + sum.longValue() + ". Runtime took around " + duration
                + " nanoseconds.");
    }

    
}