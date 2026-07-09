public class euler_002 {

    public static void main(String[] args) {

        long startTime = System.nanoTime();

        int sum = 0;
        
        int[] fib = new int[]{1, 1};

        while (fib[1] <= 4000000) {
            if (fib[1] % 2 == 0) {
                sum += fib[1];
            }
            int newFib = fib[0] + fib[1];
            fib[0] = fib[1];
            fib[1] = newFib;
        }

        long duration = System.nanoTime() - startTime;

        System.out.println("The sum is " + sum + ". Runtime took around " + duration + " nanoseconds.");
    }
    
}
