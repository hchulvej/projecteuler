package Euler;

import java.io.File;
import java.math.BigInteger;
import java.util.Scanner;

public class euler_013 {
    
    private static Scanner sc = null;

    public static void main(String[] args) {

        long startTime = System.nanoTime();
        
        try {
            sc = new Scanner(new File("D:\\Java\\Euler\\projecteuler\\euler_013.txt"));
        } catch (Exception e) {
            e.printStackTrace();
        }

        BigInteger sum = BigInteger.ZERO;
        
        while (sc.hasNextLine()) {
            BigInteger addend = new BigInteger(sc.nextLine());
            sum = sum.add(addend);
        }

        String res = sum.toString().substring(0, 10);

        long duration = System.nanoTime() - startTime;

        System.out.println("The first ten digits are " + res + ". Runtime took around " + duration
                + " nanoseconds.");
    }
    
    
    
}
