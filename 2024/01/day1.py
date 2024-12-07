def partOne():
    l1.sort()
    l2.sort()
    ans = 0
    for i in range(0, len(l1)):
        ans += abs(l1[i] - l2[i])
    print(f"Part one: {ans}")


def partTwo():
    inv = {}
    for num in l2:
        if num in inv.keys():
            inv[num] = inv[num] + 1
        else:
            inv[num] = 1
    ans = 0
    for el in l1:
        if el in inv.keys():
            ans += el * inv[el]
    print(f"Part two: {ans}")


def main():
    partOne()
    partTwo()


if __name__ == "__main__":
    main()

