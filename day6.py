import time
from concurrent import futures

import numpy as np


def finish_route(direction, x, y, data):
    path_sum = 1
    visited = [(x, y)]
    directions = [direction]
    visited_tiles = [(x, y, direction)]

    while True:
        next_move_x, next_move_y = x, y
        if direction == 0:
            next_move_x -= 1
        elif direction == 1:
            next_move_y += 1
        elif direction == 2:
            next_move_x += 1
        else:
            next_move_y -= 1

        if next_move_x < 0 or next_move_y < 0 or next_move_x >= data.shape[0] or next_move_y >= data.shape[1]:
            break

        if data[next_move_x][next_move_y] == "#":
            direction = (direction + 1) % 4
            continue

        if not (next_move_x, next_move_y) in visited:
            path_sum += 1
        else:
            if (next_move_x, next_move_y, direction) in visited_tiles:
                return False, path_sum, visited, directions

        visited.append((next_move_x, next_move_y))
        directions.append(direction)
        visited_tiles.append((next_move_x, next_move_y, direction))

        x, y = next_move_x, next_move_y
    return True, path_sum, visited, directions


def test_new_obstruction(index):
    obstacle_x, obstacle_y = visited[index]

    if data[obstacle_x][obstacle_y] == "#" or data[obstacle_x][obstacle_y] == "^":
        return False, 0, 0

    new_obstacle = data.copy()
    new_obstacle[obstacle_x][obstacle_y] = "#"
    finished, _, _, _ = finish_route(direction, start_x, start_y, new_obstacle)

    return not finished, obstacle_x, obstacle_y


with open("data/day6.txt", "r") as file:
    data = file.readlines()
    data = [[character for character in line if character != "\n"] for line in data]
    data = np.array(data).astype(str)

x, y = None,None
for i in range(data.shape[0]):
    for ii in range(data.shape[1]):
        if data[i][ii] == "^":
            x = i
            y = ii
            break
    else:
        continue
    break

start_x, start_y = x, y
direction = 0

finished, path_sum, visited, directions = finish_route(direction, x, y, data)

obstacles = []
with futures.ProcessPoolExecutor() as executor:
    futures_list = [
        executor.submit(test_new_obstruction, index)
        for index in range(1, len(visited))
    ]
    for future in futures.as_completed(futures_list):
        try:
            loop, next_move_x, next_move_y = future.result()
            if loop:
                if (next_move_x, next_move_y) in obstacles:
                    continue
                obstacles.append((next_move_x, next_move_y))
        except Exception as exc:
            continue

print(path_sum)
print(len(obstacles))
