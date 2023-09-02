import java.util.*;

public class euler_012 {
    
    private static int noOfFactors(long n) {
        List<Integer> factors = new ArrayList<Integer>();
        factors.add(1);
        factors.add(n);

        for (int i = 2; i < n; i++) {
            
        }

        return factors.size();
    }

    public static void main(String[] args) {
        
        long startTime = System.nanoTime();

        

        long duration = System.nanoTime() - startTime;

        System.out.println("The first triangle number with more than 100 factors is " + triNum(n) + ". Runtime took around " + duration
                + " nanoseconds.");
    }
}
