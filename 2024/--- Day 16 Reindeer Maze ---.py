puzzle = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

puzzle = puzzle.split("\n")
puzzle = [list(row) for row in puzzle]

# process into dict
R = len(puzzle)
C = len(puzzle[0])
labyrinth = {}
for r in range(R):
    for c in range(C):
        if puzzle[r][c] != "#":
            labyrinth[(r, c)] = []
            if puzzle[r][c] == "S":
                start = (r, c)
            if puzzle[r][c] == "E":
                end = (r, c)
for (r, c) in labyrinth:
    labyrinth[(r, c)] = [()]
del R, C, r, c

# calculate adjacent nodes, prune where none found
for pos in labyrinth:
    for dir in labyrinth[pos]:
        next = (pos[0] + dir[0], pos[1] + dir[1])
        if next in labyrinth:
            labyrinth[pos][dir] = next
    del dir, next
    labyrinth[pos] = {dir: labyrinth[pos][dir]
                      for dir in labyrinth[pos] if labyrinth[pos][dir] is not None}
del pos

################################################################################
# PART 1

all_paths = []
paths_to_check = [[start]]
while paths_to_check != []:
    p = paths_to_check.pop(0)
    pos = p[-1]
    for dir in labyrinth[pos]:
        tmp = p.copy()
        tmp.append(labyrinth[pos][dir])
        if next != end:
            paths_to_check.append(tmp)
        else:
            all_paths.append(tmp)

print(all_paths)
