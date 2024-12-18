def read_puzzle_input(filename: str) -> list:
    lines = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                sub = ['.', '.', '.']
                for char in line:
                    if char != '\n':
                        sub.append(char)
                    else:
                        break
                sub.extend(['.', '.', '.'])
                lines.append(sub)
            length = len(lines[0])
            buffer = chars = ['.' for _ in range(length)]
            for i in range(0, 3):
                lines.insert(i, buffer)
                lines.append(buffer)
        return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")


def find_starting_positions(lines: list, symbol: str):
    starting_positions = []
    for i in range(3, len(lines) - 3):
        for j in range(3, len(lines[0]) - 3):
            if lines[i][j] == symbol:
                starting_positions.append([i, j])
    return starting_positions


def get_four_chars(lines, row, col, row_delta, col_delta):
    return ''.join(lines[row + i * row_delta][col + i * col_delta] for i in range(4))


def solve_part_one(lines: list):
    starting_positions = find_starting_positions(lines, 'X')
    solution = 0
    directions = [
        (0, -1),  # north
        (1, -1),  # north-east
        (1, 0),  # east
        (1, 1),  # south-east
        (0, 1),  # south
        (-1, 1),  # south-west
        (-1, 0),  # west
        (-1, -1)  # north-west
    ]
    for position in starting_positions:
        row, col = position[0], position[1]
        for row_delta, col_delta in directions:
            word = get_four_chars(lines, row, col, row_delta, col_delta)
            if word == "XMAS":
                solution += 1
    print(f"Solution to part one: {solution}")


def get_three_chars(lines, row, col, diagonals):
    return [
        f"{lines[row + d[0]][col + d[1]]}A{lines[row + d[2]][col + d[3]]}"
        for d in diagonals
    ]


def solve_part_two(lines: list):
    starting_positions = find_starting_positions(lines, 'A')
    solution = 0
    diagonals = [
        (-1, -1, 1, 1),
        (1, -1, -1, 1)
    ]
    for pos in starting_positions:
        words = get_three_chars(lines, pos[0], pos[1], diagonals)
        if all(word == "MAS" or word[::-1] == "MAS" for word in words):
            solution += 1
    print(f"Solution to part two: {solution}")


def main():
    lines = read_puzzle_input('input.txt')
    solve_part_one(lines)
    solve_part_two(lines)


if __name__ == "__main__":
    main()
