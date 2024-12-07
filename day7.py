from concurrent import futures
from itertools import product


def all_combinations(size, operators):
    for combination in product(operators, repeat=size):
        yield list(combination)


def concat(total, number):
    return int(str(total) + str(number))


def get_evaluation(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "*":
        return number1 * number2
    elif operator == "|":
        return concat(number1, number2)
    return number1


def check_test_value(value, numbers):
    safe = None
    safe_with_concat = None
    for combination in all_combinations(len(numbers) - 1, "+*"):
        total = numbers[0]
        for number, operator in zip(numbers[1:], combination):
            total = get_evaluation(total, number, operator)
        if total == value:
            safe = (value, numbers, combination)
            break
    for combination in all_combinations(len(numbers) - 1, "+*|"):
        total = numbers[0]
        for number, operator in zip(numbers[1:], combination):
            total = get_evaluation(total, number, operator)
        if total == value:
            safe_with_concat = (value, numbers, combination)
            break
    return safe, safe_with_concat


data = []
with open("data/day7.txt", "r") as f:
    for line in f.readlines():
        line = line.split(":")
        data.append((int(line[0]), [int(n) for n in line[1].strip().split(" ")]))

safe = []
safe_with_concat = []
with futures.ProcessPoolExecutor() as executor:
    futures_list = [
        executor.submit(check_test_value, value, numbers) for value, numbers in data
    ]
    for future in futures.as_completed(futures_list):
        try:
            safe_result, safe_with_concat_result = future.result()
            if safe_result:
                safe.append(safe_result)
            if safe_with_concat_result:
                safe_with_concat.append(safe_with_concat_result)
        except Exception as exc:
            continue

total_sum = sum(safe[:][0])
for key, _, _ in safe:
    total_sum += key

total_sum_with_concat = 0
for key, _, _ in safe_with_concat:
    total_sum_with_concat += key

print(total_sum)
print(total_sum_with_concat)
