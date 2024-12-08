import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;

class Solver {
    long solution;
    List<Integer> input;
    public Solver(long solution, List<Integer> input) {
        this.solution = solution;
        this.input = input;
    }

    public long handleOperator(char operator, long tempValue, int nextValue) {
        switch (operator) {
            case '+':
                return tempValue + nextValue;
            case '*':
                return tempValue * nextValue;
            case '|':
                return Long.parseLong(tempValue + "" + nextValue);
            default:
                return tempValue;
        }
    }

    public boolean solvePartOne(char symbol, int index, long tempValue) {
        if (index == input.size() && tempValue == solution) {
            return true;
        }
        if (index < input.size()) {
            tempValue = handleOperator(symbol, tempValue, input.get(index));
            return solvePartOne('*', index + 1, tempValue) || solvePartOne('+', index + 1, tempValue);
        }
        return false;
    }

    public boolean solvePartTwo(char symbol, int index, long tempValue) {
        if (index == input.size() && tempValue == solution) {
            return true;
        }
        if (index < input.size()) {
            tempValue = handleOperator(symbol, tempValue, input.get(index));
            return solvePartTwo('*', index + 1, tempValue)
                    || solvePartTwo('+', index + 1, tempValue)
                    || solvePartTwo('|', index + 1, tempValue);
        }
        return false;
    }
}

class AocDay7 {

    public static void main(String[] args) {
        Map<Long, List<Integer>> inv = ReadInput.readFileToMap();
        long ansPartOne = 0;
        for (long key : inv.keySet()) {
            Solver solver = new Solver(key, inv.get(key));
            ansPartOne += (solver.solvePartOne('*', 1, solver.input.get(0))
                    || solver.solvePartOne('+', 1, solver.input.get(0))) ? key : 0;
        }
        System.out.println("Answer part 1: " + ansPartOne);

        long ansPartTwo = 0;
        for (long key : inv.keySet()) {
            Solver solver = new Solver(key, inv.get(key));
            ansPartTwo += (solver.solvePartTwo('*', 1, solver.input.get(0))
                    || solver.solvePartTwo('+', 1, solver.input.get(0))
                    || solver.solvePartTwo('|', 1, solver.input.get(0))) ? key : 0;
        }
        System.out.println("Answer part 2: " + ansPartTwo);
    }
}

class ReadInput {
    public static Map<Long, List<Integer>> readFileToMap() {
        List<String> lines = new ArrayList<>();
        int maxLength = 0;
        try (BufferedReader reader = new BufferedReader(new FileReader("input.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                lines.add(line);
                maxLength = Math.max(maxLength, line.length());
            }
        } catch (IOException e) {
            System.out.println("Error reading file");
        }
        Map<Long, List<Integer>> resultMap = new HashMap<>();
        for (String line : lines) {
            String[] parts = line.split(":");
            long key = Long.parseLong(parts[0].trim());

            String[] numbers = parts[1].trim().split("\\s+");
            List<Integer> values = Arrays.stream(numbers)
                    .map(Integer::parseInt)
                    .collect(Collectors.toList());

            resultMap.put(key, values);
        }
        return resultMap;
    }
}
