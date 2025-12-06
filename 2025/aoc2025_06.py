
def prepare_data_part_one() -> list[list[str]]:
    with open('data.csv') as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(' '.join(line.strip().split()).split(' '))
        print(puzzle_data)
    return puzzle_data

def solve_part_one():
    puzzle_data = prepare_data_part_one()
    total = 0
    for i in range(0, len(puzzle_data[0])):
            sub_total = int(puzzle_data[0][i])
            for j in range(1, len(puzzle_data) - 1):
                if puzzle_data[-1][i] == '*':
                    sub_total *= int(puzzle_data[j][i])
                else:
                    sub_total += int(puzzle_data[j][i])
            total += sub_total
    print(total)

def prepare_data_part_two() -> list[list[str]]:
    with open('data.csv') as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append([e for e in line.replace('\n', '')])

        buffer = len(puzzle_data[0]) - len(puzzle_data[-1])
        for i in range(0, buffer):
            puzzle_data[-1].append(' ')

    for i in range(0, len(puzzle_data[0])):
        for j in range(0, len(puzzle_data) - 1):
            if puzzle_data[j][i] != ' ':
                b = i
                while puzzle_data[-1][b] == ' ':
                    b -= 1
                puzzle_data[-1][i] = puzzle_data[-1][b]
    return puzzle_data

def solve_part_two():
    puzzle_data = prepare_data_part_two()
    for l in puzzle_data:
        print(l)
    total = 0
    op = 0
    while op < len(puzzle_data[-1]):
        if puzzle_data[-1][op] in ['*', '+']:
            num = ''
            for i in range(0, len(puzzle_data) - 1):
                num += puzzle_data[i][op]
            sub_total = int(num)
            op += 1
            while op < len(puzzle_data[-1]) and puzzle_data[-1][op] in ['*', '+']:
                num = ''
                for i in range(0, len(puzzle_data) - 1):
                    num += puzzle_data[i][op]
                if puzzle_data[-1][op] == '+':
                    sub_total += int(num)
                else:
                    sub_total *= int(num)
                op += 1
            total += sub_total
        else:
            op += 1
    print(total)

def main():
    solve_part_one()
    solve_part_two()

if __name__ == "__main__":
    main()
