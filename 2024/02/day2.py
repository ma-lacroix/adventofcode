def read_puzzle_input(filename: str):
    try:
        with open(filename, 'r') as file:
            lines = [[int(num) for num in line.strip().split(" ")] for line in file]
        return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except IOError as e:
        print(f"Error reading file: {e}")


def is_safe(level):
    inc, dec, maxd = True, True, float("-inf")
    for i in range(1, len(level)):
        dec = dec and (level[i - 1] > level[i])
        inc = inc and (level[i - 1] < level[i])
        maxd = max(maxd, abs(level[i - 1] - level[i]))
    return (inc or dec) and 1 <= maxd <= 3


def valid_lines_part1(lines: list):
    ans = 0
    for line in lines:
        ans += 1 if is_safe(line) else 0
    print(f"Part 1: {ans}")


def valid_lines_part2(lines: list):
    ans = 0
    for line in lines:
        if not is_safe(line):
            for i in range(0, len(line)):
                temp_list = [x for index, x in enumerate(line) if index != i]
                if is_safe(temp_list):
                    ans += 1
                    break
        else:
            ans += 1
    print(f"Part 2: {ans}")


def main():
    text = read_puzzle_input("aoc2024_2.txt")
    valid_lines_part1(text)
    valid_lines_part2(text)


if __name__ == "__main__":
    main()

