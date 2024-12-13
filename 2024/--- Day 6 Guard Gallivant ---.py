from tqdm import tqdm

map = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

with open("2024/inputs/6.txt") as f:
    map = f.read()

map = map.split("\n")
map = [list(line) for line in map]

R = len(map)
C = len(map[0])
# print("Map size: R =", R, ", C =", C)

# find guard
start_pos = None
guard_found = False
for r in range(R):
    for c in range(C):
        if map[r][c] == "^":
            start_pos = (r, c)
            guard_found = True
            break
    if guard_found:
        break
del guard_found
# print("Starting position of guard:", start_pos)

obstacles = [(r, c) for r in range(R) for c in range(C) if map[r][c] == "#"]
del map
# print("List of obstacles:", obstacles)

################################################################################
# PART 1

pos = start_pos
dir = (-1, 0)

unique_locations = [start_pos]
while True:

    next = (pos[0] + dir[0], pos[1] + dir[1])
    if (0 <= next[0] and next[0] < R) and (0 <= next[1] and next[1] < C):

        # next step is on the map, check if need to turn
        if next in obstacles:
            dir = (dir[1], -dir[0])
        else:
            pos = next
            if pos not in unique_locations:
                unique_locations.append(pos)
    else:
        # guard moves off the map, ending patrol
        break

print("Number of unique locations:", len(unique_locations))

################################################################################
# PART 2

# idea I: put obstruction to pos only if the guard visited, because it makes no sense to check for a location which was not encountered in the original path
unique_locations.remove(start_pos)

good_locations = []
for loc in tqdm(unique_locations):

    obstacles.append(loc)

    pos = start_pos
    dir = (-1, 0)

    # idea II: log only the turns, so no need to check every step of the new path
    turns = []

    while True:

        next = (pos[0] + dir[0], pos[1] + dir[1])
        if (0 <= next[0] and next[0] < R) and (0 <= next[1] and next[1] < C):

            # next step is on the map, check if need to turn
            if next in obstacles:
                dir = (dir[1], -dir[0])

                # we started looping, break
                if (pos, dir) in turns:
                    good_locations.append(loc)
                    break
                else:
                    turns.append((pos, dir))
            else:
                pos = next

        else:
            # guard moves off the map, ending patrol
            # obstacle at loc is not good
            break

    obstacles.remove(loc)

print("Number of possible obstructions:", len(good_locations))
