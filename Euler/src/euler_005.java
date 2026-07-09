public class euler_005 {

    public static void main(String[] args) {

        long startTime = System.nanoTime();

        
        int[] primes = new int[]{2,3,5,7,11,13,17,19};
        int[] multiplicities = new int[primes.length];

        for (int i = 2; i < 21; i++) {
            for (int j = 0; j < primes.length; j++) {
                int num = i;
                if (primes[j] <= num) {
                    int c = 0;
                    while (num % primes[j] == 0) {
                        c++;
                        num /= primes[j];
                    }
                    multiplicities[j] = Math.max(multiplicities[j], c);
                }
            }
        }

        int res = 1;
        for (int j = 0; j < primes.length; j++) {
            for (int m = 0; m < multiplicities[j]; m++) {
                res *= primes[j];
            }
            
        }

        long duration = System.nanoTime() - startTime;

        System.out.println("The smallest number is " + res + ". Runtime took around " + duration + " nanoseconds.");
        
    }

}