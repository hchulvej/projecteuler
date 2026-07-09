package Euler;

import java.math.BigInteger;

public class euler_016 {

    private static int sumOfDigits(String str) {
        int res = 0;
        String[] arr = str.split("");
        for (String s : arr) {
            res += Integer.parseInt(s);
        }
        return res;
    }

    public static void main(String[] args) {

        long startTime = System.nanoTime();

        BigInteger twoBI = new BigInteger("2");
        BigInteger pow2 = twoBI.pow(1000);

        int res = sumOfDigits(pow2.toString());

        long duration = System.nanoTime() - startTime;

        System.out.println("The sum of the digits of 2^1000 is "
                + res + ". Runtime took around " + duration
                + " nanoseconds.");
    }
}
