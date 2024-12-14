import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


class Solver {

    int rounds;
    int[] board;
    List<Robot> robots;
    int[] quadrants;
    List<Integer> validRounds;
    public Solver(int rounds, int[] board, List<Robot> robots) {
        this.rounds = rounds;
        this.board = board;
        this.robots = robots;
        this.quadrants = new int[]{0,0,0,0};
    }

    public void partOne() {
        int round = 0;
        while (round < rounds) {
            for (Robot robot : robots) {
                robot.updatePosition();
            }
            round++;
        }
        for (Robot robot : robots) {
            if (robot.currentPos[0] < board[0] / 2 && robot.currentPos[1] < board[1] / 2) {
                quadrants[0]++;
            }
            if (robot.currentPos[0] < board[0] / 2 && robot.currentPos[1] > board[1] / 2) {
                quadrants[1]++;
            }
            if (robot.currentPos[0] > board[0] / 2 && robot.currentPos[1] < board[1] / 2) {
                quadrants[2]++;
            }
            if (robot.currentPos[0] > board[0] / 2 && robot.currentPos[1] > board[1] / 2) {
                quadrants[3]++;
            }
        }
        System.out.println("Part One: " + quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]);
    }

    public int printPositions(int round) {
        char[][] picture = new char[board[0]][board[1]];
        for (int i = 0; i < board[0]; i++) {
            for (int j = 0; j < board[1]; j++) {
                picture[i][j] = '.';
            }
        }
        for (Robot robot : robots) {
            picture[robot.currentPos[0]][robot.currentPos[1]] = '0';
        }

        for (int i = 0; i < board[0]; i++) {
            String fullString = Arrays.toString(picture[i]);
            if (fullString.contains("0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0")) {
                for (int j = 0; j < board[0]; j++) {
                    for (int k = 0; k < board[1]; k++) {
                        System.out.print(picture[j][k]);
                    }
                    System.out.println();
                }
                return round;
            }
        }
        return -1;
    }

    public void partTwo() {
        int round = 1;
        while (round < rounds) {
            for (Robot robot : robots) {
                robot.updatePosition();
            }
            if(printPositions(round) != -1) {
                printPositions(round);
                System.out.println("Solution part two: " + round);
                break;
            }
            round++;
        }
    }
}


class AocDay14 {
    public static void main(String[] args) throws InterruptedException {
        int[] board = new int[]{101,103};
        List<Robot> robots = ReadInput.readFileToList(board);
        Solver solver = new Solver(50000, board, robots);
        solver.partOne();

        List<Robot> robots2 = ReadInput.readFileToList(board);
        Solver solver2 = new Solver(50000, board, robots2);
        solver2.partTwo();
    }
}

class Robot {

    public int[] tileSize;
    public int[] currentPos;
    public int[] velocity;

    public Robot(int[] tileSize, int[] currentPos, int[] velocity) {
        this.tileSize = tileSize;
        this.currentPos = currentPos;
        this.velocity = velocity;
    }

    public void updatePosition() {
        int[] newPos = new int[2];
        newPos[0] = currentPos[0] + velocity[0];
        newPos[1] = currentPos[1] + velocity[1];
        if (newPos[0] < 0) {
            newPos[0] += tileSize[0];
        }
        if (newPos[1] < 0) {
            newPos[1] += tileSize[1];
        }
        if (newPos[0] >= tileSize[0]) {
            newPos[0] -= tileSize[0];
        }
        if (newPos[1] >= tileSize[1]) {
            newPos[1] -= tileSize[1];
        }
        currentPos = newPos;
    }
}

// this part was mostly generated with GenAI
class ReadInput {
    public static List<Robot> readFileToList(int[] tileSize) {
        List<Robot> robots = new ArrayList<>();

        try (BufferedReader reader = new BufferedReader(new FileReader("/Users/mlacroix/Documents/git/adventofcode/2024/14/input.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(" ");

                String[] posStr = parts[0].substring(2).split(",");
                int[] position = new int[]{
                        Integer.parseInt(posStr[0]),
                        Integer.parseInt(posStr[1])
                };

                String[] velStr = parts[1].substring(2).split(",");
                int[] velocity = new int[]{
                        Integer.parseInt(velStr[0]),
                        Integer.parseInt(velStr[1])
                };

                robots.add(new Robot(tileSize, position, velocity));
            }
            return robots;
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
