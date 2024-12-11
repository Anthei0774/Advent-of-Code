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

    while (i < len(layout)) and (type(layout[i]) != int):
        i += 1

    if i == len(layout):
        break

    free_space = layout[i]

    assert type(layout[-1]) == tuple

    if layout[-1][1] == free_space:
        layout[i] = layout[-1]
        layout = layout[:-1]
    elif layout[-1][1] < free_space:
        layout[i] -= layout[-1][1]
        layout.insert(i, layout[-1])
        layout = layout[:-1]
    else:
        layout[i] = (layout[-1][0], free_space)
        layout[-1] = (layout[-1][0], layout[-1][1] - free_space)

    if type(layout[-1]) != tuple:
        layout = layout[:-1]

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
l = len(layout)

id = layout[-1]
j = layout.index(id)

while True:

    need_space = 1
    while (j + need_space < l) and (layout[j] == layout[j + need_space]):
        need_space += 1
    # print("Need:", layout[j: j + need_space])

    i = layout.index("")
    while True:

        free_space = 0
        while (i + free_space < l) and (layout[i] == layout[i + free_space]):
            free_space += 1
        # print("Free:", free_space)

        if need_space <= free_space:
            for k in range(need_space):
                layout[i + k] = layout[j + k]
                layout[j + k] = ""
            break
        else:
            if "" in layout[i + free_space:]:
                i = layout.index("", i + free_space)

                if j < i:
                    # print("Cannot move block")
                    break
            else:
                break

    id -= 1
    if id == -1:
        break
    else:
        j = layout.index(id)

        if "" not in layout[:j]:
            break

        print(j)

layout = [value if value != "" else 0 for value in layout]
print("Checksum:", sum(i * layout[i] for i in range(l)))
