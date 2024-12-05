def count_sum(orders):
    sum_of_fixed = 0
    for order in orders:
        sum_of_fixed += order[int(len(order) / 2)]
    return sum_of_fixed


rules = {i: [] for i in range(100)}
with open("data/day5_1.txt", "r") as file:
    for line in file.readlines():
        rule, number = line.split("|")
        rules[int(rule)].append(int(number))

with open("data/day5_2.txt", "r") as file:
    data = []
    for line in file.readlines():
        line = line.removesuffix("\n")
        data.append([
            int(number) for number in line.split(",")
        ])

proper_order = []
not_proper_order = []
for order in data:
    bad = False
    for index, number in enumerate(reversed(order)):
        previous = order[0:len(order) - index - 1]
        if any(previous_number in rules[number] for previous_number in previous):
            not_proper_order.append(order)
            break
    else:
        proper_order.append(order)

sum_of_proper = count_sum(proper_order)

fixed_order = []
for order in not_proper_order:
    changing_order = order.copy()
    bad = True
    while bad:
        bad=False
        for index, number in enumerate(reversed(changing_order)):
            previous = changing_order[0:len(changing_order) - index - 1]
            if any(previous_number in rules[number] for previous_number in previous):
                bad = True

                for previous_number in previous:
                    if previous_number in rules[number]:
                        changing_order.remove(previous_number)
                        changing_order.insert(len(changing_order) - index, previous_number)
                        break
                break
    fixed_order.append(changing_order)


sum_of_fixed = count_sum(fixed_order)

print(sum_of_proper)
print(sum_of_fixed)
