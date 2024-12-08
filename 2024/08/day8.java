import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

class Solver {

    char[][] board;
    int rows;
    int cols;
    Map<Character, List<Integer[]>> antennaPositions;
    public Solver(char[][] board) {
        this.board = board;
        this.rows = board.length;
        this.cols = board[0].length;
        this.antennaPositions = getAntennaPositions();
    }

    private Map<Character, List<Integer[]>> getAntennaPositions() {
        // Create a Map of each antenna as a key, with the list of pairs defining their locations
        Map<Character, List<Integer[]>> antennaPositions = new HashMap<>();
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                char frequency = board[row][col];
                if (Character.isLetterOrDigit(frequency)) {
                    antennaPositions.computeIfAbsent(frequency, k -> new ArrayList<>())
                            .add(new Integer[]{row, col});
                }
            }
        }
        return antennaPositions;
    }

    private Integer[] calculateAntiNodePosition(Integer[] antennaOne, Integer[] antennaTwo, boolean reverse, int jump) {
        // Calculate the slope and the next node, can be used in both cases by tweaking the jump variable 
        Integer[] diff = new Integer[2];
        Integer[] newPosition = new Integer[2];
        diff[0] = antennaTwo[0] - antennaOne[0];
        diff[1] = antennaTwo[1] - antennaOne[1];
        if (reverse) {
            newPosition[0] = antennaOne[0] - diff[0] * jump;
            newPosition[1] = antennaOne[1] - diff[1] * jump;
        } else {
            newPosition[0] = antennaTwo[0] + diff[0] * jump;
            newPosition[1] = antennaTwo[1] + diff[1] * jump;
        }
        return newPosition;
    }

    private boolean isWithinLimits(Integer[] position) {
        return position[0] >= 0 && position[0] < rows && position[1] >= 0 && position[1] < cols;
    }

    private int numberOfAntinodesForFrequency(Map<Integer, Set<Integer>> inv) {
        // Returns the total number of antinodes from the map
        return inv.values().stream().mapToInt(Set::size).sum();
    }

    public void solvePartOne() {
        // Holds a map of each unique antinode coordinates with X as the key and a Set for the Y frequencies
        Map<Integer, Set<Integer>> inv = new HashMap<>();
        for (char key: antennaPositions.keySet()) {
            List<Integer[]> positions = antennaPositions.get(key);
            for (int i = 0; i < positions.size() - 1; i++) {
                for (int j = i + 1; j < positions.size(); j++) {
                    for (boolean flag : new boolean[]{true, false}) {
                        Integer[] antiNode = calculateAntiNodePosition(positions.get(i), positions.get(j), flag, 1);
                        if (isWithinLimits(antiNode)) {
                            inv.computeIfAbsent(antiNode[0], k -> new HashSet<>()).add(antiNode[1]);
                        }
                    }
                }
            }
        }
        System.out.println("Part One solution: " + numberOfAntinodesForFrequency(inv));
    }

    public void solvePartTwo() {
        // Same as part one, but we iterate using the jump factor
        Map<Integer, Set<Integer>> inv = new HashMap<>();
        for (char key: antennaPositions.keySet()) {
            List<Integer[]> positions = antennaPositions.get(key);
            for (int i = 0; i < positions.size() - 1; i++) {
                for (int j = i + 1; j < positions.size(); j++) {
                    for (boolean flag : new boolean[]{true, false}) {
                        int jump = 0; // zero because two aligned towers are antinodes to each other!
                        while(isWithinLimits(calculateAntiNodePosition(positions.get(i), positions.get(j), flag, jump))) {
                            Integer[] antiNode = calculateAntiNodePosition(positions.get(i), positions.get(j), flag, jump);
                            inv.computeIfAbsent(antiNode[0], k -> new HashSet<>()).add(antiNode[1]);
                            jump++;
                        }
                    }
                }
            }
        }
        System.out.println("Part Two solution: " + numberOfAntinodesForFrequency(inv));
    }

}

class AocDay8 {
    public static void main(String[] args) {
        char[][] board = ReadInput.readFileToArray();
        Solver solver = new Solver(board);
        solver.solvePartOne();
        solver.solvePartTwo();
    }
}

class ReadInput {
    // This part was 98% generated with Cody AI.

    public static char[][] readFileToArray() {
        List<String> lines = new ArrayList<>();
        int maxLength = 0;
        try (BufferedReader reader = new BufferedReader(
                new FileReader("/Users/mlacroix/Documents/git/adventofcode/2024/08/input.txt"))
        ) {
            String line;
            while ((line = reader.readLine()) != null) {
                lines.add(line);
                maxLength = Math.max(maxLength, line.length());
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        char[][] array = new char[lines.size()][maxLength];
        for (int i = 0; i < lines.size(); i++) {
            String line = lines.get(i);
            for (int j = 0; j < maxLength; j++) {
                if (j < line.length()) {
                    array[i][j] = line.charAt(j);
                } else {
                    array[i][j] = ' ';
                }
            }
        }
        return array;
    }
}
