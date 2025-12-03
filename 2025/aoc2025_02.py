

def solve_part_one(data: list[list]):
    invalid_numbers = []
    for r in data:
        start = int(r[0])
        end = int(r[1])
        while start <= end:
            start_string = str(start)
            if start_string[0:int(len(start_string)/2)] == start_string[int(len(start_string)/2):]:
                invalid_numbers.append(start)
            start += 1
    print(sum(invalid_numbers))


def solve_part_two(data: list[list]):
    invalid_numbers = set()
    for r in data:
        start = int(r[0])
        end = int(r[1])
        while start <= end:
            start_string = str(start)
            for i in range(0, len(start_string)):
                if len(start_string.replace(start_string[0:i],"")) == 0:
                    invalid_numbers.add(start)
            start += 1
    print(sum(invalid_numbers))


def main():
    numbers = ("655-1102,2949-4331,885300-1098691,1867-2844,20-43,4382100-4484893,781681037-781860439,647601-734894,"
               "2-16,180-238,195135887-195258082,47-64,4392-6414,6470-10044,345-600,5353503564-5353567532,124142-198665,"
               "1151882036-1151931750,6666551471-6666743820,207368-302426,5457772-5654349,72969293-73018196,71-109,"
               "46428150-46507525,15955-26536,65620-107801,1255-1813,427058-455196,333968-391876,482446-514820,"
               "45504-61820,36235767-36468253,23249929-23312800,5210718-5346163,648632326-648673051,116-173,"
               "752508-837824").split(',')
    puzzle_data = [e.split('-') for e in numbers]
    solve_part_one(puzzle_data)
    solve_part_two(puzzle_data)

if __name__ == "__main__":
    main()
