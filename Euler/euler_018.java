package Euler;

import java.io.File;
import java.util.ArrayList;
import java.util.Scanner;

public class euler_018 {

    public static void main(String[] args) {

        String path = "D:\\Java\\Euler\\projecteuler\\euler_018.txt";

        int[][] triangle = null;
        ArrayList<String[]> lines = new ArrayList<>();

        Scanner sc = null;

        try {
            sc = new Scanner(new File(path));
            while (sc.hasNextLine()) {
                lines.add(sc.nextLine().split(" "));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        lines.stream().forEach(line -> System.out.println(line));
    }

}
