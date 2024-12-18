def read_puzzle_input_dag() -> dict:
    file_name = "input_dag.txt"
    puzzle_map = {}
    with open(file_name, 'r') as file:
        for line in file:
            key_val = [int(num) for num in line.replace('\n', '').split('|')]
            if key_val[0] not in puzzle_map:
                puzzle_map[key_val[0]] = []
            if key_val[1] in puzzle_map:
                puzzle_map.get(key_val[1]).append(key_val[0])
            else:
                puzzle_map[key_val[1]] = [key_val[0]]
    return puzzle_map


def read_puzzle_input_pages() -> list:
    file_name = "input_pages.txt"
    lines = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                lines.append([int(num) for num in line.replace('\n', '').split(',')])
        return lines
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found")


def get_valid_instructions(pmap: dict, pages: list) -> list:
    valid_pages = []
    for page in pages:
        good = True
        for i, element in enumerate(page):
            for value in pmap.get(element):
                j = i + 1
                while j < len(page):
                    if page[j] == value:
                        good = False
                    j += 1
                if not good:
                    break
        if good:
            valid_pages.append(page)
    return valid_pages


def get_invalid_instructions(pmap: dict, pages: list) -> list:
    invalid_pages = []
    for page in pages:
        good = True
        for i, element in enumerate(page):
            for value in pmap.get(element):
                j = i + 1
                while j < len(page):
                    if page[j] == value:
                        good = False
                    j += 1
        if not good:
            invalid_pages.append(page)
    return invalid_pages


def get_score_per_element(values: list, page: list) -> int:
    score = 0
    for num in page:
        if num in values:
            score += 1
    return score


def generate_right_order(pmap: dict, pages: list) -> list:
    answer = []
    for page in pages:
        scores = {}
        for num in page:
            scores[num] = get_score_per_element(pmap[num], page)
        answer.append([k for k, v in sorted(scores.items(), key=lambda x: x[1])])
    return answer


def print_solution(pages: list, name: str):
    solution = 0
    for page in pages:
        solution += page[int(len(page) / 2)]
    print(f"{name}: {solution}")


def main():
    puzzle_map = read_puzzle_input_dag()
    input_pages = read_puzzle_input_pages()
    pages = get_valid_instructions(puzzle_map, input_pages)
    print_solution(pages, "Part one")
    invalid_pages = get_invalid_instructions(puzzle_map, input_pages)
    corrected = generate_right_order(puzzle_map, invalid_pages)
    print_solution(corrected, "Two: ")


if __name__ == "__main__":
    main()
