package Euler;

import java.util.ArrayList;
import java.util.List;

public class Primes {
    
    private static boolean[] sieve;
    private static int upperLimit;

    public Primes(int ul) {
        upperLimit = ul;
        sieve = new boolean[ul];
        for (int i = 2; i < ul; i++) {
            sieve[i] = true;
        }
        update();
    }

    private static void update() {
        for (int i = 2; i < upperLimit; i++) {
            if (sieve[i]) {
                int m = 2;
                while (m * i < upperLimit) {
                    sieve[m * i] = false;
                    m++;
                }
            }
        }
    }

    public static void expand() {
        int newUpperLimit = 100 * upperLimit;
        boolean[] newSieve = new boolean[newUpperLimit];
        for (int i = 0; i < upperLimit; i++) {
            newSieve[i] = sieve[i];
        }
        upperLimit = newUpperLimit;
        sieve = newSieve;
        update();
    }

    public static List<Integer> getPrimeNumbers() {
        List<Integer> res = new ArrayList<Integer>();

        for (int i = 2; i < upperLimit; i++) {
            if (sieve[i]) {
                res.add(i);
            }
        }

        return res;
    }

    public static boolean[] getSieve() {
        return sieve;
    }

    public static int getUpperLimit() {
        return upperLimit;
    }
}
