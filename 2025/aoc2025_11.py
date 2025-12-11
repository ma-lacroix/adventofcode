from collections import deque


def generate_dataset() -> dict[list]:
    paths = {}
    with open('data.csv') as f:
        for line in f:
            key = line.strip().split(':')[0]
            values = line.strip().split(': ')[1].split(' ')
            paths[key] = values
    return paths

def solve_part_one():
    paths = generate_dataset()
    q = deque()
    total_valid_paths = 0
    q.append('you')
    seen = set()
    while len(q) > 0:
        current_key = q.popleft()
        if current_key == 'out':
            total_valid_paths += 1
        else:
            seen.add(current_key)
        for node in paths.get(current_key,[]):
            q.append(node)
    print(total_valid_paths)


def solve(paths: dict, current_path: set, current_key: str, memo=None) -> int:
    # Note: I cheated with an LLM for caching ideas

    if memo is None:
        memo = {}
    has_fft = 'fft' in current_path
    has_dac = 'dac' in current_path
    state_key = (current_key, has_fft, has_dac)
    if state_key in memo:
        return memo[state_key]
    if current_key == 'out':
        return 1 if has_fft and has_dac else 0
    total = 0
    for p in paths.get(current_key, []):
        if p not in current_path:
            new_current_path = current_path.copy()
            new_current_path.add(p)
            total += solve(paths, new_current_path, p, memo)
    memo[state_key] = total
    return total

def solve_part_two():
    paths = generate_dataset()
    current_path = set()
    current_path.add('svr')
    total_valid_paths = solve(paths, current_path, 'svr')
    print(total_valid_paths)


def main():
    solve_part_one()
    solve_part_two()

if __name__ == "__main__":
    main()
