

def solve_part_two(directions: list, moves: list):
    current = 50
    total_passes = 0
    for i in range(len(directions)):
        total_passes += moves[i] // 100
        if directions[i] == 'L':
            current = (current - moves[i]) % 100
        else:
            current = (current + moves[i]) % 100
        if current == 0:
            total_passes += 1
    print(total_passes)


def solve_part_one(directions: list, moves: list):
    current = 50
    stops_at_zero = 0
    for i in range(len(directions)):
        if directions[i] == 'L':
            current = (current - moves[i]) % 100
        else:
            current = (current + moves[i]) % 100
        if current == 0:
            stops_at_zero += 1
    print(stops_at_zero)



def main():
    # part 1
    directions = []
    moves = []
    with open('data.csv') as f:
        for line in f:
            l = line.replace('\n','')
            directions.append(l[0])
            moves.append(int(l[1:]))
    solve_part_one(directions, moves)
    solve_part_two(directions, moves)

    # part 2


if __name__ == "__main__":
    main()