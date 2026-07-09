package Euler;

import java.math.BigInteger;

public class euler_015 {
    
    //Any combination of r-d-d-r-r-d-d-d-r-...-d (20 r's and 20 d's)
    //Answer is binom(40,20) = (40 * 39 * ... * 21)

    public static void main(String[] args) {

        long startTime = System.nanoTime();
        
        BigInteger fac20 = BigInteger.ONE;
        BigInteger fac40 = BigInteger.ONE;
        for (int i = 2; i <= 40; i++) {
            if (i < 21) {
                String v = Integer.toString(i);
                fac20 = fac20.multiply(new BigInteger(v));
                fac40 = fac40.multiply(new BigInteger(v));            
            } else {
                String v = Integer.toString(i);
                fac40 = fac40.multiply(new BigInteger(v));
            }
        }

        BigInteger res = (fac40.divide(fac20)).divide(fac20);

        long duration = System.nanoTime() - startTime;

        System.out.println("There are "
                + res + " such routes. Runtime took around " + duration
                + " nanoseconds.");
    }
    



}
