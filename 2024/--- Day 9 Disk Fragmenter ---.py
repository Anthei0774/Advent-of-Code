diskmap = """2333133121414131402"""

with open("2024/inputs/9.txt") as f:
    diskmap = f.read()

diskmap = list(map(int, diskmap))
assert len(diskmap) % 2 == 1

# process
layout_orig = []
id = 0
for i in range(0, len(diskmap), 2):

    layout_orig.append((id, diskmap[i]))
    id += 1

    if (i != len(diskmap) - 1) and (diskmap[i + 1] != 0):
        layout_orig.append(diskmap[i + 1])

################################################################################
# PART 1

layout = layout_orig.copy()

i = 0
while True:

    # find first free space. If no gap, step out
    while (i < len(layout)) and (type(layout[i]) != int):
        i += 1
    if i == len(layout):
        break
    free_space = layout[i]

    # if free space is just enough, then pop last and inject into free space pos
    if layout[-1][1] == free_space:
        layout[i] = layout.pop(-1)
    # elif free space is larger, then decrement space, still popping
    elif layout[-1][1] < free_space:
        layout[i] -= layout[-1][1]
        layout.insert(i, layout.pop(-1))
    # else free space is not enough, then fill it, and decrement file size
    else:
        layout[i] = (layout[-1][0], free_space)
        layout[-1] = (layout[-1][0], layout[-1][1] - free_space)

    # if free space is last, delete it
    if type(layout[-1]) != tuple:
        layout = layout[:-1]

# checksum
S = 0
m = 0
for block in layout:
    for i in range(block[1]):
        S += (m * block[0])
        m += 1

print("Checksum:", S)

###############################################################################
# PART 2

layout = layout_orig.copy()

j = len(layout) - 1
while True:

    # search until a move candidate found
    # exit defragmentation if we pass through the layout
    while (0 <= j) and (type(layout[j]) != tuple):
        j -= 1
    if j == -1:
        break

    # start searching for free space, it cannot occur after j
    # if we reach j, then current file = layout[j] cannot be moved
    i = 0
    while (i < j) and ((type(layout[i]) != int) or (layout[i] < layout[j][1])):
        i += 1
    if i == j:
        j -= 1
        continue

    # free space is just enough, swap
    if layout[i] == layout[j][1]:
        tmp = layout[i]
        layout[i] = layout[j]
        layout[j] = tmp
    # free space is larger, fill and decrement like before
    else:
        layout[i] -= layout[j][1]
        tmp = layout[j]
        layout[j] = layout[j][1]
        layout.insert(i, tmp)

    # in this last if-else was encountered, then no need to decrement j again. On its place, and integer should be by the swap, or it is already shifted by the insert

# checksum
S = 0
m = 0
for block in layout:
    if type(block) == int:
        block = (0, block)
    for i in range(block[1]):
        S += (m * block[0])
        m += 1

print("Checksum:", S)
