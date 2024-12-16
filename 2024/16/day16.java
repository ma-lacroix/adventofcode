import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

enum Direction {
    RIGHT, DOWN, LEFT, UP;
}

class State {
    Pair position;      // The current position in the maze (x, y)
    Direction direction; // The direction you moved to reach this state
    int score;          // The total score accumulated to reach this state

    public State(Pair position, Direction direction, int score) {
        this.position = position;
        this.direction = direction;
        this.score = score;
    }
}


class Pair {
    int x;
    int y;
    public Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true; // Same object
        if (obj == null || getClass() != obj.getClass()) return false; // Null or different class
        Pair pair = (Pair) obj;
        return x == pair.x && y == pair.y; // Compare x and y values
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y); // Combine x and y for hash code
    }

}

class Solver {

    char[][] board;
    Pair start;
    Pair end;
    int bestPath;
    Map<Pair, List<Pair>> graph;

    public Solver(char[][] board) {
        this.board = board;
        this.start = null;
        this.end = null;
        this.graph = generateGraph();
        this.bestPath = Integer.MAX_VALUE;
    }

    private List<Pair> getAllPairs(Pair position) {
        List<Pair> pairs = new ArrayList<>();
        // right
        if (board[position.x][position.y + 1] != '#') {
            pairs.add(new Pair(position.x, position.y + 1));
        }
        // down
        if (board[position.x + 1][position.y] != '#') {
            pairs.add(new Pair(position.x + 1, position.y));
        }
        // left
        if (board[position.x][position.y - 1] != '#') {
            pairs.add(new Pair(position.x, position.y - 1));
        }
        // up
        if (board[position.x - 1][position.y] != '#') {
            pairs.add(new Pair(position.x - 1, position.y));
        }
        return pairs;
    }

    private Map<Pair, List<Pair>> generateGraph() {
        Map<Pair, List<Pair>> graph = new HashMap<>();
        for (int i = 1; i < board.length - 1; i++) {
            for (int j = 1; j < board[0].length - 1; j++) {
                if (board[i][j] != '#') {
                    if (board[i][j] == 'S') {
                        start = new Pair(i, j);
                    }
                    if (board[i][j] == 'E') {
                        end = new Pair(i, j);
                    }
                    graph.put(new Pair(i, j), getAllPairs(new Pair(i, j)));
                }
            }
        }
        return graph;
    }

    private Direction getNewDirection(Pair position, Pair newPosition) {
        // right
        if (position.x == newPosition.x && position.y + 1 == newPosition.y) {
            return Direction.RIGHT;
        }
        // down
        if (position.x + 1 == newPosition.x && position.y == newPosition.y) {
            return Direction.DOWN;
        }
        // left
        if (position.x == newPosition.x && position.y - 1 == newPosition.y) {
            return Direction.LEFT;
        }
        // up
        return Direction.UP;
    }

    public void partOne() {
        Queue<State> queue = new LinkedList<>();
        Set<Pair> visited = new HashSet<>();
        queue.add(new State(start, Direction.RIGHT, 0));
        visited.add(start);

        int minScore = Integer.MAX_VALUE;

        while (!queue.isEmpty()) {
            State current = queue.poll();
            Pair position = current.position;
            if (position.equals(end)) {
                minScore = Math.min(minScore, current.score);
                continue;
            }

            for (Pair neighbor : getAllPairs(position)) {
                if (!visited.contains(neighbor)) {
                    Direction newDirection = getNewDirection(position, neighbor);
                    int addValue = (current.direction == newDirection) ? 1 : 1001;
                    queue.add(new State(neighbor, newDirection, current.score + addValue));
                    if (!neighbor.equals(end)) {
                        visited.add(neighbor);
                    }
                }
            }
        }

        System.out.println("Part one answer: " + (minScore == Integer.MAX_VALUE ? -1 : minScore));
    }


}


class AocDay16 {
    public static void main(String[] args) {
        char[][] board = ReadInput.readFileToArray();
        Solver solver = new Solver(board);
        solver.partOne();
    }
}


class ReadInput {
    // This part was 98% generated with AI.

    public static char[][] readFileToArray() {
        List<String> lines = new ArrayList<>();
        int maxLength = 0;
        try (BufferedReader reader = new BufferedReader(
                new FileReader("/Users/mlacroix/Documents/git/adventofcode/2024/16/input.txt"))
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
