public class euler_001 {

    public static void main(String[] args) {

        long startTime = System.nanoTime();

        int sum = 0;
        
        for (int n = 3; n < 1000; n++) {
            if (n % 3 == 0) {
                sum += n;
            } else {
                if (n % 5 == 0) {
                    sum += n;
                }
            }
        }

        long duration = System.nanoTime() - startTime;

        System.out.println("The sum is " + sum + ". Runtime took around " + duration + " nanoseconds.");
    }
}