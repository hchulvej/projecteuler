public class euler_006 {

    public static void main(String[] args) {

        long startTime = System.nanoTime();

        int diff = 0;

        int[] n = new int[] { 0, 1 };
        int[] sum = new int[] { 0, 1 };
        int[] sumOfSquares = new int[] { 0, 1 };

        while (n[1] < 100) {
            n[0] = n[1];
            n[1] = n[0] + 1;
            sum[0] = sum[1];
            sum[1] = sum[0] + n[1];
            sumOfSquares[0] = sumOfSquares[1];
            sumOfSquares[1] = sumOfSquares[0] + n[1] * n[1];
            diff = sum[1] * sum[1] - sumOfSquares[1];
        }

        long duration = System.nanoTime() - startTime;

        System.out.println("The difference of the sums is " + diff + ". Runtime took around " + duration
                + " nanoseconds.");
    }

}
