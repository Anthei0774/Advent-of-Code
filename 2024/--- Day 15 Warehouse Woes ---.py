puzzle = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

puzzle = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

with open("2024/inputs/15.txt") as f:
    puzzle = f.read()

puzzle = puzzle.split("\n\n")
[warehouse, sequence] = puzzle
del puzzle

warehouse = warehouse.split("\n")
warehouse = [list(row) for row in warehouse]
R = len(warehouse)
C = len(warehouse[0])

walls = []
boxes = []
start = None
for r in range(R):
    for c in range(C):
        if warehouse[r][c] == "#":
            walls.append((r, c))
        elif warehouse[r][c] == "O":
            boxes.append((r, c))
        elif warehouse[r][c] == "@":
            start = (r, c)

sequence = sequence.replace("\n", "")

################################################################################
# PART 1

pos = start
for iter, dir in enumerate(sequence):

    if dir == ">":
        dir = (0, 1)
    elif dir == "v":
        dir = (1, 0)
    elif dir == "<":
        dir = (0, -1)
    else:
        dir = (-1, 0)

    next = None
    size = 1
    while True:
        next = (pos[0] + size * dir[0], pos[1] + size * dir[1])
        if (next in walls) or ((next not in walls) and (next not in boxes)):
            break
        else:
            size += 1

    if next in walls:
        continue

    if size == 1:
        pos = next
    else:
        pos = (pos[0] + dir[0], pos[1] + dir[1])
        boxes.remove(pos)
        boxes.append(next)

print("Sum of boxes' GPS coordinates:", sum(b[0] * 100 + b[1] for b in boxes))
