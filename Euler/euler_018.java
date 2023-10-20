package Euler;

import java.io.File;
import java.util.Scanner;

public class euler_018 {

    public static void main(String[] args) {

        String path = "D:\\Java\\Euler\\projecteuler\\euler_018.txt";

        int[][] triangle = null;
        

        Scanner sc = null;

        try {
            sc = new Scanner(new File(path));
            while (sc.hasNextLine()) {
                System.out.println(sc.nextLine());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
