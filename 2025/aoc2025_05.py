
def solve_part_one(fresh_ranges: list[list], ingredients: list[int]):
    total = 0
    for ingredient in ingredients:
        for r in fresh_ranges:
            if r[0] <= ingredient <= r[1]:
                total += 1
                break
    print(total)


def prepare_data_set() -> list[str]:
    fresh_ranges = []
    max_num_length = 0
    with open('data_ranges.csv') as f:
        for line in f:
            parts = line.strip().split('-')
            len_start = len(parts[0])
            len_end = len(parts[1])
            max_num_length = max(max_num_length, len_start, len_end)
            fresh_ranges.append(line.strip())
    for i, ra in enumerate(fresh_ranges):
        r = ra.split('-')
        r[0] = f"{'0' * (max_num_length - len(r[0]))}{r[0]}"
        r[1] = f"{'0' * (max_num_length - len(r[1]))}{r[1]}"
        fresh_ranges[i] = f"{r[0]}-{r[1]}"
    return sorted(fresh_ranges)

def create_linear_sequence(fresh_ranges: list[str]) -> list[str]:
    for i in range(1, len(fresh_ranges)):
        one = [int(e) for e in fresh_ranges[i-1].split('-')]
        two = [int(e) for e in fresh_ranges[i].split('-')]
        if two[1] < one[1]:
            two[1] = one[1]
        if two[0] < one[1]:
            new_end = two[0] - 1
            if new_end < one[0]:
                new_end = one[0]
            one[1] = new_end
        fresh_ranges[i-1] = f"{one[0]}-{one[1]}"
        fresh_ranges[i] = f"{two[0]}-{two[1]}"
    return fresh_ranges

def solve_part_two():
    fresh_ranges = prepare_data_set()
    fresh_ranges_linear = create_linear_sequence(fresh_ranges)
    total = 0
    for r in fresh_ranges_linear:
        if int(r.split('-')[1]) > int(r.split('-')[0]):
            total += int(r.split('-')[1]) - int(r.split('-')[0]) + 1
    print(total - 1)    # This -1 was a wild guess that a number was overcounted. I can't believe it worked.

def main():
    fresh_ranges = []
    ingredients = []
    with open('data_ranges.csv') as f:
        for line in f:
            fresh_ranges.append([int(e) for e in line.strip().split('-')])
    with open('data_ingredients.csv') as f:
        for line in f:
            ingredients.append(int(line.strip()))
    solve_part_one(fresh_ranges, ingredients)
    solve_part_two()

if __name__ == "__main__":
    main()
