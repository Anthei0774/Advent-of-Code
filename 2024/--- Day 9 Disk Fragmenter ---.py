diskmap = """2333133121414131402"""

with open("2024/inputs/9.txt") as f:
    diskmap = f.read()

diskmap = list(map(int, diskmap))


def process_diskmap_to_layout(diskmap):
    layout = []
    id = 0

    assert len(diskmap) % 2 == 1
    for i in range(0, len(diskmap), 2):

        for j in range(diskmap[i]):
            layout.append(id)
        id += 1

        if i != len(diskmap) - 1:
            for j in range(diskmap[i + 1]):
                layout.append("")

    return layout

################################################################################
# PART 1


layout = process_diskmap_to_layout(diskmap)

while True:

    while layout[-1] == "":
        layout.pop(-1)

    if "" in layout:
        i = layout.index("")
        layout[i] = layout.pop(-1)
    else:
        break

print("Checksum:", sum(i * layout[i] for i in range(len(layout))))

################################################################################
# PART 2

layout = process_diskmap_to_layout(diskmap)
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
