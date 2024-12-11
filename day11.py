
def apply_rules(stone: int,previous_results):
    if stone in previous_results.keys():
        return previous_results[stone],previous_results
    if stone == 0:
        return [1],previous_results
    if not len(str(stone)) % 2:
        digits = [int(digit) for digit in str(stone)]
        first_stone = digits[:len(digits) // 2]
        second_stone = digits[len(digits) // 2:]
        first_stone = int("".join(map(str, first_stone)))
        second_stone = int("".join(map(str, second_stone)))
        previous_results[stone] = [first_stone, second_stone]
        return [first_stone, second_stone],previous_results
    return [2024 * stone],previous_results

def main():
    with open("data/day11.txt", "r") as f:
        data: list[int] = [int(number) for number in f.readline().strip().split()]

    previous_results={}

    stone_line: list[int] = data.copy()
    for i in range(75):
        new_stone_line = []
        for stone in stone_line:
            v,previous_results = apply_rules(stone,previous_results)
            new_stone_line.extend(v)
        stone_line = new_stone_line
        print(i)
        print(len(stone_line))

if __name__ == "__main__":
    main()