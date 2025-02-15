import java.io.File;
import java.util.*;
import java.util.stream.Collectors;

public class euler_018 {

    private static List<Integer> reduce(List<Integer> shorter,  List<Integer> longer) {
        List<Integer> res =  new ArrayList<>();
        for (int i = 0; i< shorter.size(); i++) {
            res.add(Math.max(shorter.get(i) + longer.get(i), shorter.get(i) +   longer.get(i + 1)));
        }
        return res;
    }

    public static void main(String[] args) {

        long start = System.currentTimeMillis();

        String path = "C:\\GitHub Repos\\projecteuler\\euler_018.txt";

        ArrayList<List<Integer>> lines = new ArrayList<>();

        Scanner sc;

        try {
            sc = new Scanner(new File(path));
            while (sc.hasNextLine()) {
                List<String>  line = Arrays.asList(sc.nextLine().split(" "));
                lines.add(line.stream().map(Integer::parseInt).collect(Collectors.toList()));
            }

            Collections.reverse(lines);

        } catch (Exception e) {
            e.printStackTrace();
        }

        while (lines.size() > 1) {
            List<Integer> reduction = reduce(lines.get(1), lines.get(0));
            lines.set(1,  reduction);
            lines.removeFirst();
        }

        long end = System.currentTimeMillis();

        System.out.println("Task completed in " + (end - start) + " ms with result: " + lines.getFirst().getFirst());
    }

}
