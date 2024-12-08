from itertools import combinations

import numpy as np

data = []
with open("data/day8.txt", "r") as f:
    for line in f.readlines():
        data.append([character for character in line.strip()])

data = np.array(data)

frequencies = list(np.unique(data))
frequencies.remove(".")

antinodes = np.zeros((data.shape[0], data.shape[1])).astype(int)
antinodes_harmonics = np.zeros((data.shape[0], data.shape[1])).astype(int)

for frequency in frequencies:
    indices = list(np.where(data == frequency))
    indices = list(zip(indices[0], indices[1]))
    pairs = combinations(indices, 2)
    for pair in pairs:
        diff = (pair[0][0] - pair[1][0], pair[0][1] - pair[1][1])
        x1 = pair[0][0] + diff[0]
        y1 = pair[0][1] + diff[1]
        x2 = pair[1][0] - diff[0]
        y2 = pair[1][1] - diff[1]

        if not (x1 < 0 or x1 > data.shape[0] - 1 or y1 < 0 or y1 > data.shape[1] - 1):
            antinodes[x1, y1] = "1"
        if not (x2 < 0 or x2 > data.shape[0] - 1 or y2 < 0 or y2 > data.shape[1] - 1):
            antinodes[x2, y2] = "1"

for frequency in frequencies:
    indices = list(np.where(data == frequency))
    indices = list(zip(indices[0], indices[1]))
    pairs = combinations(indices, 2)
    for pair in pairs:
        diff = (pair[0][0] - pair[1][0], pair[0][1] - pair[1][1])
        x1, y1 = pair[0]
        x2, y2 = pair[1]
        antinodes_harmonics[x1, y1] = "1"
        antinodes_harmonics[x2, y2] = "1"
        while True:
            x1 += diff[0]
            y1 += diff[1]
            if not (
                    x1 < 0 or x1 > data.shape[0] - 1 or y1 < 0 or y1 > data.shape[1] - 1
            ):
                antinodes_harmonics[x1, y1] = "1"
            else:
                break

        x1, y1 = pair[0]
        x2, y2 = pair[1]
        while True:
            x2 -= diff[0]
            y2 -= diff[1]
            if not (
                    x2 < 0 or x2 > data.shape[0] - 1 or y2 < 0 or y2 > data.shape[1] - 1
            ):
                antinodes_harmonics[x2, y2] = "1"
            else:
                break

antinodes_sum = antinodes.sum()
antinodes_harmonics_sum = antinodes_harmonics.sum()
print(antinodes_sum)
print(antinodes_harmonics_sum)
