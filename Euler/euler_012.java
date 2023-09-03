package Euler;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class euler_012 {
    
    private static Primes p = new Primes(100);

    private static List<Integer> primes = Primes.getPrimeNumbers();

    private static int numberOfFactors(int n) {

        while (Primes.getUpperLimit() < n) {
            Primes.expand();
        }

        List<Integer> primeFactors = new ArrayList<>();
        for (int d = 0; d <= Math.min(n, primes.size() - 1); d++) {
            if (n % primes.get(d) == 0) {
                primeFactors.add(primes.get(d));
            }
        }

        int[] multiplicities = new int[primeFactors.size()];

        for (int i = 0; i < primeFactors.size(); i++) {
            int num = n;
            multiplicities[i] = 1;
            while (num % primeFactors.get(i) == 0) {
                multiplicities[i]++;
                num /= primeFactors.get(i);
            }
        }

        int res = 1;
        for (int m : multiplicities) {
            res *= m;
        }

        
        return res;
    }

    public static void main(String[] args) {

        long startTime = System.nanoTime();

        int n = 7;
        int t = 28;

        while (numberOfFactors(t) < 501) {
            n++;
            t += n;
        }

        long duration = System.nanoTime() - startTime;

        System.out.println("The first triangle number is " + t + ". Runtime took around " + duration
                + " nanoseconds.");
    }
}
