public class euler_012 {
    
    private static long triNum(long n) {
        return n * (n + 1) / 2;
    }

    private static int noOfFactors(long n) {
        int count = 0;
        for (int d = 1; d <= n; d++) {
            if (n % (long) d == 0) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        
        long startTime = System.nanoTime();

        System.out.println(noOfFactors(28));

        long duration = System.nanoTime() - startTime;

        System.out.println("The first triangle number with more than 100 factors is " + 1 + ". Runtime took around " + duration
                + " nanoseconds.");
    }
}
