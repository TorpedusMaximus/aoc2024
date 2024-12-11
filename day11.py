def apply_rules(stone: int, previous_results):
    if stone in previous_results.keys():
        return previous_results[stone]
    if not len(str(stone)) % 2:
        digits = [int(digit) for digit in str(stone)]
        first_stone = digits[:len(digits) // 2]
        second_stone = digits[len(digits) // 2:]
        first_stone = int("".join(map(str, first_stone)))
        second_stone = int("".join(map(str, second_stone)))
        previous_results[stone] = [first_stone, second_stone]
        return [first_stone, second_stone]
    return [2024 * stone]


def main():
    with open("data/day11.txt", "r") as f:
        stones = {int(stone): 1 for stone in f.readline().strip().split()}

    previous_results = {0: [1]}

    for i in range(75):
        new_stones = {}
        for stone, number in stones.items():
            results = apply_rules(stone, previous_results)
            for result in results:
                new_stones[result] = new_stones.get(result, 0) + number
        stones = new_stones
        print(i)
        print(sum(stones.values()))


if __name__ == "__main__":
    main()