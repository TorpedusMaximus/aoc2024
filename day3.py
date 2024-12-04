import re

with open("data/day3.txt", "r") as file:
    data = file.readlines()
    data = "".join(data)

found = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)", data)
total = 0
for mul in found:
    if mul == "don't()" or mul == "do()":
        continue
    result = mul.removeprefix("mul(").removesuffix(")").split(",")
    total += int(result[0]) * int(result[1])

total_with_dos = 0
do = True
for mul in found:
    if mul == "don't()":
        do = False
        continue
    if mul == "do()":
        do = True
        continue
    if do:
        result = mul.removeprefix("mul(").removesuffix(")").split(",")
        total_with_dos += int(result[0]) * int(result[1])

print(total)
print(total_with_dos)
