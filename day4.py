import numpy as np


def check_for_xmas(matrix: np.ndarray):
    def count_xmas(array: np.ndarray) -> int:
        return int("".join(array[:4]) == "SAMX") + int("".join(array[3:]) == "XMAS")

    xmas_sum = 0
    xmas_sum += count_xmas(matrix[3])
    xmas_sum += count_xmas(matrix[:, 3])
    xmas_sum += count_xmas(matrix.diagonal())
    xmas_sum += count_xmas(np.fliplr(matrix).diagonal())


def check_for_x_mas(matrix: np.ndarray):
    diagonal1 = "".join(matrix.diagonal())
    diagonal2 = "".join(np.fliplr(matrix).diagonal())

    return (diagonal1 == "MAS" or diagonal1 == "SAM") and (diagonal2 == "MAS" or diagonal2 == "SAM")


with open("data/day4.txt", "r") as file:
    data = file.readlines()
    data = [[character for character in line if character != "\n"] for line in data]

data = np.array(data).astype(str)
data = np.pad(data, ((3, 3), (3, 3)), "constant", constant_values=".")

indexes_of_x = data == "X"
xmas_sum = 0
for i in range(data.shape[0]):
    for ii in range(data.shape[1]):
        if indexes_of_x[i][ii]:
            xmas_sum += check_for_xmas(data[i - 3: i + 4, ii - 3: ii + 4])

indexes_of_a = data == "A"
x_mas_sum = 0
for i in range(data.shape[0]):
    for ii in range(data.shape[1]):
        if indexes_of_a[i][ii]:
            x_mas_sum += check_for_x_mas(data[i - 1: i + 2, ii - 1: ii + 2])

print(xmas_sum)
print(x_mas_sum)
