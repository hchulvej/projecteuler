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
        noOfPrimes = 0;
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

    public boolean[] expendPrimes() {
        int N = this.primes.length;
        boolean[] newPrimes = new boolean[10*N];
        Arrays.fill(newPrimes, true);
        for (int i = 0; i < N; i++) {
            newPrimes[i] = this.primes[i];
        }
        return newPrimes;
    }

    public int getNoOfPrimes() {
        return this.noOfPrimes;
    }

    public static void main(String[] args) {

        long startTime = System.nanoTime();

        euler_007 euler = new euler_007(1000);

        while (euler.getNoOfPrimes() < 10001) {
            euler.updatePrimes();
            euler.primes = euler.expendPrimes();
        }
        euler.updatePrimes();

        int count = 0;
        int p = 0;

        while(true) {
            if (euler.primes[p]) {
                count++;
            }
            if (count == 10001) {
                break;
            }
            p++;
        }

        long duration = System.nanoTime() - startTime;

        System.out.println("The 10001th prime is " + p + ". Runtime took around " + duration
                + " nanoseconds.");
    }

}
