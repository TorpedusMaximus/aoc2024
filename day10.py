import numpy as np


def search_for_trail(hiking_map, x, y):
    elevation = hiking_map[x, y]
    trails = 0
    peaks = []
    if elevation == 8:
        if hiking_map[x + 1, y] == 9:
            trails += 1
            peaks.append((x + 1, y))
        if hiking_map[x - 1, y] == 9:
            trails += 1
            peaks.append((x - 1, y))
        if hiking_map[x, y + 1] == 9:
            trails += 1
            peaks.append((x, y + 1))
        if hiking_map[x, y - 1] == 9:
            trails += 1
            peaks.append((x, y - 1))
    else:
        if hiking_map[x + 1, y] == elevation + 1:
            trail, peak = search_for_trail(hiking_map, x + 1, y)
            trails += trail
            peaks.extend(peak)
        if hiking_map[x - 1, y] == elevation + 1:
            trail, peak = search_for_trail(hiking_map, x - 1, y)
            trails += trail
            peaks.extend(peak)
        if hiking_map[x, y + 1] == elevation + 1:
            trail, peak = search_for_trail(hiking_map, x, y + 1)
            trails += trail
            peaks.extend(peak)
        if hiking_map[x, y - 1] == elevation + 1:
            trail, peak = search_for_trail(hiking_map, x, y - 1)
            trails += trail
            peaks.extend(peak)

    return trails, peaks


data = []
with open("data/day10.txt", "r") as f:
    for line in f.readlines():
        data.append([character if character != '.' else -1 for character in line.strip()])

data = np.pad(np.array(data).astype(int), 8, constant_values=-1)
positions = np.where(data == 0)
positions = list(zip(positions[0], positions[1]))

score,rating = 0,0
for x, y in positions:
    trails, peaks = search_for_trail(data[x - 8: x + 9, y - 8: y + 9], 8, 8)
    peaks = list(set(peaks))
    score += len(peaks)
    rating+=trails

print(score)
print(rating)
