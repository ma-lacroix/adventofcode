import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

class ReadInput {
    public static char[][] readFileToArray(String filename) throws IOException {
        List<String> lines = new ArrayList<>();
        int maxLength = 0;
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = reader.readLine()) != null) {
                lines.add(line);
                maxLength = Math.max(maxLength, line.length());
            }
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

class Solver {

    char[][] board;
    int[][] passes;
    int[] current_position;
    int[] direction;
    int totalUniqueMoves;
    boolean run;

    public Solver(char[][] board) {
        this.board = board;
        this.passes = new int[board.length][board[0].length];
        this.current_position = findStartingPosition();
        this.direction = new int[]{-1,0};
        this.totalUniqueMoves = 0;
        this.run = true;
    }

    private int[] findStartingPosition() {
        int[] current_position = new int[2];
        boolean found = false;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == '^') {
                    current_position[0] = i; current_position[1] = j;
                    found = true;
                    break;
                }
                if (found) break;
            }
        }
        return current_position;
    }

    private void turn90Degrees() {
        // up to right
        if (direction[0] == -1 && direction[1] == 0) {
            direction[0] = 0;
            direction[1] = 1;
        }
        // right to down
        else if (direction[0] == 0 && direction[1] == 1) {
            direction[0] = 1;
            direction[1] = 0;
        }
        // down to left
        else if (direction[0] == 1 && direction[1] == 0) {
            direction[0] = 0;
            direction[1] = -1;
        }
        // left to up
        else if (direction[0] == 0 && direction[1] == -1) {
            direction[0] = -1;
            direction[1] = 0;
        }
    }

    private void updatePosition(int[] nextMove) {
        // out of bounds
        if (nextMove[0] < 0
                || nextMove[1] < 0
                || nextMove[0] == board.length
                || nextMove[1] == board[0].length) {
            run = false;
        }
        // valid move
        else if (board[nextMove[0]][nextMove[1]] == '.'
                || board[nextMove[0]][nextMove[1]] == 'X') {
            current_position[0] = nextMove[0];
            current_position[1] = nextMove[1];
        }
        // turn 90 degrees
        else {
            turn90Degrees();
        }
    }

    public void getTotalUniqueMoves() {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == 'X') {
                    totalUniqueMoves++;
                }
            }
        }
    }

    public void solvePartOne() {
        while (run) {
            board[current_position[0]][current_position[1]] = 'X';
            int[] nextMove = new int[] {current_position[0] + direction[0], current_position[1] + direction[1]};
            updatePosition(nextMove);
        }
        getTotalUniqueMoves();
        System.out.println("Solution part 1: " + totalUniqueMoves);
    }

    public int solvePartTwo() {
        while (run) {
            passes[current_position[0]][current_position[1]] = passes[current_position[0]][current_position[1]] + 1;
            if (passes[current_position[0]][current_position[1]] > 4) {
                return 1;
            }
            board[current_position[0]][current_position[1]] = 'X';
            int[] nextMove = new int[] {current_position[0] + direction[0], current_position[1] + direction[1]};
            updatePosition(nextMove);
        }
        return 0;
    }
}

class AocDaySix {

    public static void main(String[] args) {
        // part one
        try {
            char[][] board = ReadInput.readFileToArray("/Users/mlacroix/Desktop/input.txt");
            Solver solver = new Solver(board);
            solver.solvePartOne();
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
        }

        // part two
        try {
            char[][] board = ReadInput.readFileToArray("/Users/mlacroix/Desktop/input.txt");
            int ans = 0;
            for (int i = 0; i < board.length; i++) {
                for (int j = 0; j < board[i].length; j++) {
                    char[][] altBoard = ReadInput.readFileToArray("/Users/mlacroix/Desktop/input.txt");
                    if (altBoard[i][j] != '#' && altBoard[i][j] != '^') {
                        altBoard[i][j] = '#';
                        Solver solver = new Solver(altBoard);
                        ans += solver.solvePartTwo();
                    }
                }
            }
            System.out.println("Solution part 2: " + ans);
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
        }
    }}
