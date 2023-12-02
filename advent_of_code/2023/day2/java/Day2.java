import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Day2 {

    public static void main(String[] args) throws IOException {
        
        List<String> input = Files.readAllLines(Path.of("input.txt"));
        int sum = 0;
        int power = 0;

        for(String game : input) {
            int id = Integer.parseInt(game.split(":")[0].split(" ")[1]);
            int[] counts = new int[]{0, 0, 0};

            String[] games = game.split(":")[1].split(";");

            for(String entry : games) {
                String[] sets = entry.trim().split(",");
                for(String set : sets){
                    String[] balls = set.trim().split(" ");

                    int number = Integer.parseInt(balls[0]);
                    String colour = balls[1];

                    if(colour.equals("red")) {
                        counts[0] = Math.max(counts[0], number);
                    } else if(colour.equals("green")) {
                        counts[1] = Math.max(counts[1], number);
                    } else if(colour.equals("blue")) {
                        counts[2] = Math.max(counts[2], number);
                    }
                }
            }
            
            if(counts[0] <= 12 && counts[1] <= 13 && counts[2] <= 14) {
                sum += id;
            }

            power += counts[0] * counts[1] * counts[2];
        }

        System.out.println("part 1: " + sum);
        System.out.println("part 2: " + power);
    }

}