package Euler;

public class euler_014 {

    private static long next(long n) {
        if (n % 2 == 0) {
            return n / 2;
        } else {
            return 3 * n + 1;
        }
    }

    private static long chainLength(long n) {
        long cl = 1;
        while (n > 1) {
            cl++;
            n = next(n);
        }
        return cl;
    }

    public static void main(String[] args) {

        long startTime = System.nanoTime();

        long longestChain = -1;
        long startingNumber = 0;
        for (long n = 2; n < 1000000; n++) {
            long cl = chainLength(n);
            if (cl > longestChain) {
                startingNumber = n;
                longestChain = cl;
            }
        }

        long duration = System.nanoTime() - startTime;

        System.out.println("The starting number, under one million, which produces the longest chain, is "
                + startingNumber + ". Runtime took around " + duration
                + " nanoseconds.");
    }

}
