from collections import deque


def prepare_data_p1() -> list[list[str]]:
    puzzle_data = []
    with open('data.csv') as f:
        for line in f:
            puzzle_data.append([e for e in line.strip()])
    return puzzle_data

def solve_part_one():
    active_beams = set()
    total_splits = 0
    puzzle_data = prepare_data_p1()
    active_beams.add(int(len(puzzle_data[0])/2))
    for i in range(1, len(puzzle_data)):
        for j in range(0, len(puzzle_data[i])):
            if puzzle_data[i][j] == '^' and j in active_beams:
                # found a splitter
                total_splits += 1
                active_beams.discard(j)
                active_beams.add(j - 1)
                active_beams.add(j + 1)
    print(total_splits)

def prepare_data_p2() -> list[list[str]]:
    puzzle_data = []
    with open('data.csv') as f:
        for line in f:
            if line.strip() != len(line.strip()) * '.':
                puzzle_data.append([e for e in line.strip()])
    return puzzle_data

def create_graph(puzzle_data: list[list[str]]) -> dict:
    paths = {}
    active_beams = set()
    active_beams.add(int(len(puzzle_data[0]) / 2))
    queue = deque()
    start_node = f"0-{int(len(puzzle_data[0]) / 2)}"
    paths[start_node] = []
    queue.append(start_node)
    seen = set()
    while len(queue) > 0:
        current = queue.pop()
        seen.add(current)
        paths[current] = []
        if int(current.split('-')[0]) == len(puzzle_data): break
        for i in range(int(current.split('-')[0]) + 1, len(puzzle_data)):
            if puzzle_data[i][int(current.split('-')[1])] == '^':
                new_path_one = f"{i}-{int(current.split('-')[1]) - 1}"
                new_path_two = f"{i}-{int(current.split('-')[1]) + 1}"
                paths[current].append(new_path_one)
                paths[current].append(new_path_two)
                if new_path_one not in seen:
                    queue.append(new_path_one)
                if new_path_two not in seen:
                    queue.append(new_path_two)
                break
    return paths


def solve(paths: dict, current_node: str, cache: dict = None) -> int:
    # can't use the @cache decorator
    if cache is None:
        cache = {}
    if current_node in cache:
        return cache[current_node]

    if 0 == len(paths[current_node]):
        return 1  # Reached leaf!!!
    total_paths = 0
    for path in paths[current_node]:
        total_paths += solve(paths, path, cache)
    cache[current_node] = total_paths
    return total_paths


def solve_part_two():
    puzzle_data = prepare_data_p2()

    # create Graph:
    paths = create_graph(puzzle_data)
    starting_node = f"0-{int(len(puzzle_data[0]) / 2)}"

    # recursion
    total = solve(paths, starting_node)
    print(total)


def main():
    # solve_part_one()
    solve_part_two()

if __name__ == "__main__":
    main()
