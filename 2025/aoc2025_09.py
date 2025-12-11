# INCOMPLETE SOLUTION


def prepare_data_p1() -> list[list[int]]:
    nums = []
    with open('data.csv') as f:
        for line in f:
            nums.append([int(e) for e in line.strip().split(',')])
    return nums

def solve_part_one():
    puzzle_data = prepare_data_p1()
    max_size = -1
    for i in range(0, len(puzzle_data)):
        for j in range(i, len(puzzle_data)):
            if i == j:
                continue
            x1 = puzzle_data[i][0]
            x2 = puzzle_data[j][0]
            y1 = puzzle_data[i][1]
            y2 = puzzle_data[j][1]
            if x1 <= x2:
                x2 += 1
            else:
                x1 += 1
            if y1 <= y2:
                y2 += 1
            else:
                y1 += 1
            max_size = max((abs(x1 - x2)* abs(y1 - y2)), max_size)
    print(max_size)

def solve_part_two():
    pass


def main():
    solve_part_one()
    solve_part_two()

if __name__ == "__main__":
    main()
