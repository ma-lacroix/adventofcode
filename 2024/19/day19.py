
def backtrack_one(w: str, t: list) -> bool:
    if len(w) == 0:
        return True
    for towel in t:
        if w.startswith(towel):
            if backtrack_one(w.removeprefix(towel), t):
                return True
    return False


def solve_part_one(s: list, t: list) -> None:
    answer = 0
    for seq in s:
        if backtrack_one(seq, t):
            answer += 1
    print(f"Part one: {answer}")


def backtrack_two(w: str, t: list, v: int, memo) -> int:
    if w in memo:
        return memo[w] + v
    if len(w) == 0:
        return v + 1
    count = v
    for towel in t:
        if w.startswith(towel):
            count = backtrack_two(w.removeprefix(towel), t, count, memo)
    memo[w] = count - v
    return count


def solve_part_two(s: list, t: list) -> None:
    answer = 0
    i = 0
    for seq in s:
        answer += backtrack_two(seq, t, 0, {})
    print(f"Part two: {answer}")


def get_towels() -> list:
    file_name = "towels.txt"
    towels = []
    with open(file_name, 'r') as file:
        for line in file:
            towels = line.replace(' ', '').split(',')
    return towels


def get_sequences() -> list:
    file_name = "sequences.txt"
    sequences = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                sequences.append(line.replace('\n', ''))
        return sequences
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found")


def main():
    s = get_sequences()
    t = get_towels()
    solve_part_one(s, t)
    solve_part_two(s, t)


if __name__ == "__main__":
    main()
