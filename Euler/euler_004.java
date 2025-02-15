public class euler_004 {

    private boolean isPalindrome(String num) {
        StringBuilder sb = new StringBuilder(num);
        sb.reverse();
        return num.equals(sb.toString());
    }

    public static void main(String[] args) {

        long startTime = System.nanoTime();

        euler_004 euler = new euler_004();

        int largestPalindrome = -1;

        for (int n = 100; n < 1000; n++) {
            for (int m = n; m < 1000; m++) {
                 if (euler.isPalindrome(Integer.toString(n * m))) {
                    largestPalindrome = Math.max(largestPalindrome, n * m);
                }
            }
        }

        long duration = System.nanoTime() - startTime;

        System.out.println("The largest palindrome is " + largestPalindrome + ". Runtime took around " + duration + " nanoseconds.");
    }
                

}

                

