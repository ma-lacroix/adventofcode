from functools import cache


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

"""    
solve(digits, start_index, left_digits) - returns best result for digits[start_index:] with left_digits

    = 0 if start_index >= len(digits) and left_digits != 0
    = max(digits[start_index:])  if left_digits == 1
    = max(
        1. pick digits[start_index] and recurse with start_index+1, left_digits-1
            digits[start_index] * (10 ** left_digits) + solve(digits, start_index+1, left_digits-1)
            
        2. don't pick digits[start_index] and recurse with start_index+1, left_digits
            solve(digits, start_index+1, left_digits)
    )
"""

@cache
def solve(digits: tuple[int], start_index: int, left_digits: int) -> int:
    if start_index >= len(digits):
        return float('-inf')

    if left_digits == 1:
        return max(digits[start_index:])

    return max(
        digits[start_index] * int(10 ** (left_digits - 1)) + solve(digits, start_index+1, left_digits-1),
        solve(digits, start_index+1, left_digits)
    )

def solve_part_two(data: list[list]):
    total = 0
    for d in data:
        digits = [int(e) for e in str(d)]
        best = solve(tuple(digits), 0, 12)
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
