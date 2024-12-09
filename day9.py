def is_empty(val):
    return val == '.' or val == -1


with open("data/day9.txt", "r") as file:
    data = file.readline()
    data = [int(character) for character in data.strip()]

blocks = []
blocks_meta = []  # index in blocks, length, value
index = 0
for i in range(0, len(data), 2):
    blocks_meta.append([len(blocks), data[i], index])
    blocks.extend([index] * data[i])
    index += 1
    if i + 1 < len(data):
        blocks_meta.append([len(blocks), data[i + 1], -1])
        blocks.extend(['.'] * data[i + 1])

blocks_fragmented = blocks[:]
for i in range(len(blocks_fragmented) - 1, -1, -1):
    if is_empty(blocks_fragmented[i]):
        continue
    for ii in range(0, i):
        if is_empty(blocks_fragmented[ii]):
            blocks_fragmented[ii] = blocks_fragmented[i]
            blocks_fragmented[i] = "."
            break

blocks_defragmented = blocks[:]
for file_index, (start, size, value) in reversed(list(enumerate(blocks_meta))):
    if is_empty(value):
        continue
    for empty_index, (empty_start, empty_size, empty_val) in enumerate(blocks_meta[:file_index]):
        if not is_empty(empty_val):
            continue
        if empty_size >= size:
            blocks_defragmented[start:start + size] = ["."] * size
            blocks_defragmented[empty_start:empty_start + size] = [value] * size
            blocks_meta[empty_index][0] += size
            blocks_meta[empty_index][1] -= size
            break

blocks_sum = sum(index * val for index, val in enumerate(blocks_fragmented) if val != '.')
blocks_defragmented_sum = sum(index * int(val) for index, val in enumerate(blocks_defragmented) if val != '.')

print(blocks_sum)
print(blocks_defragmented_sum)
