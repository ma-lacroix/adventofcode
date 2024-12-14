import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;


class Solver {

    List<MachineBehavior> behaviors;
    List<List<long[]>> validMoves;

    public Solver(List<MachineBehavior> behaviors) {
        this.behaviors = behaviors;
        this.validMoves = new ArrayList<>();
    }

//    Button A: X+94, Y+34
//    Button B: X+22, Y+67
//    Prize: X=8400, Y=5400

    private boolean isValidMove(long pushA, long pushB, MachineBehavior behavior, long bonus) {
        long x = bonus + behavior.prize[0] - (long) behavior.buttonA[0] * pushA - (long) behavior.buttonB[0] * pushB;
        long y = bonus + behavior.prize[1] - (long) behavior.buttonA[1] * pushA - (long) behavior.buttonB[1] * pushB;
        return x == 0 && y == 0;
    }

    private void findValidMoves(long bonus) {
        for (int i = 0; i < behaviors.size(); i++) {
            validMoves.add(new ArrayList<>());
            long maxButtonA = Math.max((bonus + behaviors.get(i).prize[0])/behaviors.get(i).buttonA[0], (bonus + behaviors.get(i).prize[1])/behaviors.get(i).buttonA[1]);
            long maxButtonB = Math.max((bonus + behaviors.get(i).prize[0])/behaviors.get(i).buttonB[0], (bonus + behaviors.get(i).prize[1])/behaviors.get(i).buttonB[1]);
            for (long j = 0; j<= maxButtonA; j++) {
                for (long k = maxButtonB; 0 <= k; k--) {
                    if (isValidMove(j, k, behaviors.get(i), bonus)) {
                        validMoves.get(i).add(new long[]{j, k});
                    }
                }
            }
        }
    }

    public void partOne() {
        findValidMoves(0L);
        long answer = 0;
        for (List<long[]> validMove : validMoves) {
            if (validMove.isEmpty()) continue;
            long minTokens = Integer.MAX_VALUE;
            for (long[] ints : validMove) {
                minTokens = Math.min(minTokens, ints[0] * 3 + ints[1]);
            }
            answer += minTokens;
        }
        System.out.println("Part one solution: " + answer);
    }

    public void partTwo() {
        findValidMoves(10000000000000L);
        long answer = 0;
        for (List<long[]> validMove : validMoves) {
            if (validMove.isEmpty()) continue;
            long minTokens = Integer.MAX_VALUE;
            for (long[] ints : validMove) {
                minTokens = Math.min(minTokens, ints[0] * 3 + ints[1]);
            }
            answer += minTokens;
        }
        System.out.println("Part two solution: " + answer);
    }

}


class AocDay13 {
    public static void main(String[] args) {
        List<MachineBehavior> behaviors = ReadInput.readFileToArray();
        Solver solver = new Solver(behaviors);
        solver.partOne();
//        solver.partTwo();
    }
}


// These last two boilerplate classes were mostly generated with AI

class MachineBehavior {
    int[] buttonA;
    int[] buttonB;
    int[] prize;

    public MachineBehavior(String[] input) {
        buttonA = parseButton(input[0]);
        buttonB = parseButton(input[1]);
        prize = parsePrize(input[2]);
    }

    private int[] parseButton(String line) {
        String[] parts = line.split(":");
        String[] coords = parts[1].trim().split(",");
        return new int[] {
                Integer.parseInt(coords[0].trim().substring(2)),
                Integer.parseInt(coords[1].trim().substring(2))
        };
    }

    private int[] parsePrize(String line) {
        String[] parts = line.split(":");
        String[] coords = parts[1].trim().split(",");
        return new int[] {
                Integer.parseInt(coords[0].trim().substring(2)),
                Integer.parseInt(coords[1].trim().substring(2))
        };
    }
}

class ReadInput {

    public static List<MachineBehavior> readFileToArray() {
        List<MachineBehavior> behaviors = new ArrayList<>();

        String[] group = new String[3];
        int groupIndex = 0;

        try (BufferedReader reader = new BufferedReader(new FileReader("/Users/mlacroix/Documents/git/adventofcode/2024/13/input.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (line.trim().isEmpty()) {
                    if (groupIndex > 0) {
                        behaviors.add(new MachineBehavior(group));
                        groupIndex = 0;
                    }
                    continue;
                }
                group[groupIndex++] = line;
                if (groupIndex == 3) {
                    behaviors.add(new MachineBehavior(group));
                    groupIndex = 0;
                }
            }
            if (groupIndex == 3) {
                behaviors.add(new MachineBehavior(group));
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return behaviors;
    }
}
