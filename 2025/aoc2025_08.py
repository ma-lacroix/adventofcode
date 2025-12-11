# INCOMPLETE SOLUTION

from collections import deque


def prepare_data_p1() -> list[list[int]]:
    nums = []
    with open('data.csv') as f:
        for line in f:
            nums.append([int(e) for e in line.strip().split(',')])
    return nums

def solve_part_one():
    puzzle_data = prepare_data_p1()

    # prepare graph
    graph = {}
    for i in range(len(puzzle_data)):
        # Convert current node to string key
        current_node_key = str(puzzle_data[i])

        # Initialize list if not present
        if current_node_key not in graph:
            graph[current_node_key] = set()

        best_dist_sq = float('inf')  # Use infinity for initial comparison
        best_node_key = ""

        for j in range(len(puzzle_data)):
            if i == j:
                continue

            # FIX 2: math optimization (Squared Euclidean Distance)
            # Remove sqrt and abs. It yields the same "closest" result but faster.
            dx = puzzle_data[i][0] - puzzle_data[j][0]
            dy = puzzle_data[i][1] - puzzle_data[j][1]
            dz = puzzle_data[i][2] - puzzle_data[j][2]

            dist_sq = dx ** 2 + dy ** 2 + dz ** 2

            if dist_sq < best_dist_sq:
                best_dist_sq = dist_sq
                best_node_key = str(puzzle_data[j])
        graph[current_node_key].add(best_node_key)
        if best_node_key not in graph:
            graph[best_node_key] = set()

        graph[best_node_key].add(current_node_key)

    for k in graph.keys():
        print(f"{k} -> {graph[k]}")

    # BFS
    seen = set()
    circuits = []
    for k in ['[162, 817, 812]','[425, 690, 689]']:
    # for k in graph.keys():
        if k in seen:
            continue
        q = deque()
        q.append(k)
        seen.add(k)
        boxes = 0
        while len(q) > 0:
            current = q.popleft()
            boxes += 1
            for node in list(graph[current]):
                if node not in seen:
                    seen.add(node)
                    q.append(node)
        circuits.append(boxes)
    print(sorted(circuits))

def solve_part_two():
    pass


def main():
    solve_part_one()
    solve_part_two()

if __name__ == "__main__":
    main()
