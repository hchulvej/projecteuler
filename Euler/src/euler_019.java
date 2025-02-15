package Euler;

import java.util.Calendar;

public class euler_019 {

    public static void main(String[] args) {
        long time = System.currentTimeMillis();
        int count = 0;
        for (int i = 1901; i <= 2000; i++) {
            for (int j = 1; j <= 12; j++) {
                Calendar cal = Calendar.getInstance();
                cal.set(i, j, 1);
                if (cal.get(Calendar.DAY_OF_WEEK) == Calendar.SUNDAY) {
                    count++;
                }
            }
        }
        System.out.println(count);
        System.out.println("Time: " + (System.currentTimeMillis() - time) + "ms");
    }
}