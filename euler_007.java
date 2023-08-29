import java.util.Arrays;

public class euler_007 {

    private boolean[] primes;
    private int noOfPrimes = 0;

    public euler_007(int initialSize) {
        primes = new boolean[initialSize];
        Arrays.fill(primes, true);
        primes[0] = false;
        primes[1] = false;
    }

    public void updatePrimes() {
        for (int i = 0; i < this.primes.length; i++) {
            if (primes[i]) {
                noOfPrimes++;
                int m = 2;
                while(m * i < this.primes.length) {
                    primes[m * i] = false;
                    m++;
                }
            }
        }
    }

    public int getNoOfPrimes() {
        return this.noOfPrimes;
    }

    public static void main(String[] args) {

        long startTime = System.nanoTime();

        euler_007 euler = new euler_007(100);
        euler.updatePrimes();

        int np = euler.getNoOfPrimes();

        long duration = System.nanoTime() - startTime;

        System.out.println("The 10001th prime is " + np + ". Runtime took around " + duration
                + " nanoseconds.");
    }

}
