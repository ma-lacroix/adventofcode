import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;


class Solver {
    int[][] topoMap;
    boolean[][] visited;
    List<int[]> heads;
    int totalPaths;
    int[] dx = {0, 1, 0, -1};
    int[] dy = {-1, 0, 1, 0};

    public Solver(int[][] topoMap) {
        this.topoMap = topoMap;
        this.visited = new boolean[topoMap.length][topoMap[0].length];
        this.totalPaths = 0;
        this.heads = findAllHeads();
    }

    private void resetVisited() {
        visited = new boolean[topoMap.length][topoMap[0].length];
    }

    private List<int[]> findAllHeads() {
        List<int[]> heads = new ArrayList<>();
        for (int i = 0; i < topoMap.length; i++) {
            for (int j = 0; j < topoMap[0].length; j++) {
                if (topoMap[i][j] == 0) {
                    heads.add(new int[]{i, j});
                }
            }
        }
        return heads;
    }

    private boolean inBounds(int[] nextMove) {
        return nextMove[0] >= 0 && nextMove[0] < topoMap.length
                && nextMove[1] >= 0 && nextMove[1] < topoMap[0].length;
    }

    private boolean validMove(int[] nextMove, int[] position) {
        if (inBounds(nextMove)) {
            int currentHeight = topoMap[position[0]][position[1]];
            int nextHeight = topoMap[nextMove[0]][nextMove[1]];
            return !visited[nextMove[0]][nextMove[1]]
                    && nextHeight - currentHeight == 1;
        }
        return false;
    }

    private void recursion(int[] position, boolean partOne) {
        if (topoMap[position[0]][position[1]] == 9) {
            if (partOne) {
                visited[position[0]][position[1]] = true;
            }
            totalPaths++;
            return;
        }
        for (int i = 0; i < 4; i++) {
            int[] nextMove = new int[]{position[0] + dx[i], position[1] + dy[i]};
            if (validMove(nextMove, position)) {
                recursion(nextMove, partOne);
            }
        }
    }

    public void solvePartOne() {
        totalPaths = 0;
        for (int[] head : heads) {
            resetVisited();
            recursion(head, true);
        }
        resetVisited();
        System.out.println("Part one: " + totalPaths);
    }

    public void solvePartTwo() {
        totalPaths = 0;
        for (int[] head : heads) {
            recursion(head, false);
        }
        System.out.println("Part two: " + totalPaths);
    }

}

class AocDay10 {
    public static void main(String[] args) {
        int[][] topoMap = ReadInput.readFileToArray();
        Solver solver = new Solver(topoMap);
        solver.solvePartOne();
        solver.solvePartTwo();
    }
}

class ReadInput {
    // This part was 98% generated with AI.

    public static int[][] readFileToArray() {
        List<String> lines = new ArrayList<>();
        int maxLength = 0;
        try (BufferedReader reader = new BufferedReader(
                new FileReader("/Users/mlacroix/Documents/git/adventofcode/2024/10/input.txt"))
        ) {
            String line;
            while ((line = reader.readLine()) != null) {
                lines.add(line);
                maxLength = Math.max(maxLength, line.length());
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        int[][] array = new int[lines.size()][maxLength];
        for (int i = 0; i < lines.size(); i++) {
            String line = lines.get(i);
            for (int j = 0; j < maxLength; j++) {
                if (j < line.length()) {
                    array[i][j] = Character.getNumericValue(line.charAt(j));
                } else {
                    array[i][j] = ' ';
                }
            }
        }
        return array;
    }
}
