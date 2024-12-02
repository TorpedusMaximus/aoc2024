import numpy as np

with open("data/day1.txt", 'r') as file:
    data = file.readlines()

values = [line.split("   ") for line in data]
a1 = np.array(sorted(int(val[0]) for val in values))
a2 = np.array(sorted(int(val[1]) for val in values))

a = np.abs(a2 - a1)
diff = a.sum()

s = list(set(a1) & set(a2))

a_filtered = [number for number in a1 if number in s]

similarity=0
for number in a_filtered:
    numb_count = a2[a2 == number].size
    similarity += numb_count*number

print(diff)
print(similarity)