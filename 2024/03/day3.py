import re


def read_puzzle_input(filename: str):
    try:
        with open(filename, 'r') as file:
            lines = ""
            for line in file:
                lines += line
        return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")


def partOne(text: str) -> None:
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, text)
    ans = 0
    for match in matches:
        ans += int(match[0]) * int(match[1])
    print(f"Solution to part 1: {ans}")


def createBooleanArray(text: str) -> list:
    dos = r"do\(\)"
    donts = r"don\'t\(\)"  # Matches the literal don't()
    dos_positions = list(re.finditer(dos, text))
    donts_positions = list(re.finditer(donts, text))
    i = 0
    j = 0
    k = 0
    ok = []
    while i < len(dos_positions) and j < len(donts_positions):
        if dos_positions[i].start() < donts_positions[j].start():
            i += 1
            while k < donts_positions[j].start():
                ok.append(True)
                k += 1
        else:
            j += 1
            while k < dos_positions[i].start():
                ok.append(False)
                k += 1
    if dos_positions[-1].start() < donts_positions[-1].start():
        while k < len(text):
            ok.append(False)
            k += 1
    else:
        while k < len(text):
            ok.append(True)
            k += 1
    return ok


def mul(num1: int, num2: int):
    return num1 * num2


def partTwo(text: str) -> None:
    function_calls = r"mul\((\d+),(\d+)\)"
    functions = re.finditer(function_calls, text)
    ans = 0
    ok = createBooleanArray(text)
    for match in functions:
        if ok[match.start()]:
            ans += eval(match.group(0))
    print(f"Solution to part 2: {ans}")


def main():
    text = read_puzzle_input("input.txt")
    partOne(text)
    partTwo("do()" + text)


if __name__ == "__main__":
    main()
