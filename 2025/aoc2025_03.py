def solve_part_one(data: list[list]):
    total = 0
    for d in data:
        digits = [int(e) for e in str(d)]
        l = len(digits)
        ind_val = [9999999999, -1]
        for i in range(0, l - 1):
            if ind_val[1] < digits[i]:
                ind_val[0] = i
                ind_val[1] = digits[i]
        j = l - 1
        second_digit = -1
        while ind_val[0] < j:
            second_digit = digits[j] if second_digit < digits[j] else second_digit
            j -= 1
        total += int(f"{ind_val[1]}{second_digit}")
    print(total)

def solve(digits: list[int], local: list[int], start_index: int, current_best: int) -> int:
    if len(local) == 12:
        return int(''.join(map(str, local)))
    if len(digits) - start_index < 12 - len(local):
        return 0
    for i in range(start_index, len(digits)):
        new_local = local.copy()    # Meh. Don't like that but works.
        new_local.append(digits[i])
        if str(new_local[0]) < str(current_best)[0]:
            continue
        result_sum = solve(digits, new_local, i + 1, current_best)
        current_best = max(result_sum, current_best)
    return current_best

def solve_part_two(data: list[list]):
    total = 0
    for d in data:
        digits = [int(e) for e in str(d)]
        best = solve(digits, [], 0, 0)
        print(best)
        total += best
    print(total)


def main():
    puzzle_data = []
    with open('data.csv') as f:
        for line in f:
            puzzle_data.append(line.replace('\n',''))
    # solve_part_one(puzzle_data)
    solve_part_two(puzzle_data)

if __name__ == "__main__":
    main()
