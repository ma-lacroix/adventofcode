
def solve_part_one(data: list[list]):
    total = 0
    for row in range(1, len(data) - 1):
        for col in range(1, len(data[0]) - 1):
            if data[row][col] != '@':
                continue
            around = 0
            if data[row - 1][col - 1] == '@': around += 1
            if data[row - 1][col] == '@': around += 1
            if data[row - 1][col + 1] == '@': around += 1
            if data[row][col - 1] == '@': around += 1
            if data[row][col + 1] == '@': around += 1
            if data[row + 1][col - 1] == '@': around += 1
            if data[row + 1][col] == '@': around += 1
            if data[row + 1][col + 1] == '@': around += 1
            if around < 4: total += 1
    print(total)

def handle_clean_up(data: list[list], elements_to_check: list[list]) -> [int, list[list], list[list]]:
    total = 0
    elements_to_check_again = []
    for row in range(1, len(data) - 1):
        for col in range(1, len(data[0]) - 1):
            if data[row][col] != '@':
                continue
            around = 0
            if data[row - 1][col - 1] == '@': around += 1
            if data[row - 1][col] == '@': around += 1
            if data[row - 1][col + 1] == '@': around += 1
            if data[row][col - 1] == '@': around += 1
            if data[row][col + 1] == '@': around += 1
            if data[row + 1][col - 1] == '@': around += 1
            if data[row + 1][col] == '@': around += 1
            if data[row + 1][col + 1] == '@': around += 1
            if around < 4:
                total += 1
                elements_to_check_again.append([row, col])
    for e in elements_to_check_again:
        data[e[0]][e[1]] = '.'
    return total, elements_to_check_again, data

def solve_part_two(data: list[list]):
    elements_to_check = []
    total = 0
    for row in range(1, len(data) - 1):
        for col in range(1, len(data[0]) - 1):
            elements_to_check.append([row, col])
    round_changes, new_elements_to_check, new_board = handle_clean_up(data, elements_to_check)
    total += round_changes
    while len(new_elements_to_check) > 0:
        round_changes, new_elements_to_check, new_board = handle_clean_up(data, elements_to_check)
        total += round_changes
    print(total)


def main():
    puzzle_data = []
    with open('data.csv') as f:
        i = 0
        for line in f:
            line = line.replace('\n', '')
            line = f".{line}."
            chars = [char for char in line]
            if i == 0:
                # adding buffer around the board
                puzzle_data.append([char for char in '.' * len(chars)])
            puzzle_data.append(chars)
            i += 1
    puzzle_data.append([char for char in '.' * len(puzzle_data[0])])
    solve_part_one(puzzle_data)
    solve_part_two(puzzle_data)

if __name__ == "__main__":
    main()
