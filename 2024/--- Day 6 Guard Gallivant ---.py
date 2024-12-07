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

# memorization for part 2
original_path = [(pos, dir)]
unique_locations = {pos: 0}

i = 1
while True:

    # append new location with direction

    next = (pos[0] + dir[0], pos[1] + dir[1])
    if (0 <= next[0] and next[0] < R) and (0 <= next[1] and next[1] < C):

        # next step is on the map, check if need to turn
        if next in obstacles:
            dir = (dir[1], -dir[0])
        else:
            pos = next
            if pos not in unique_locations:
                unique_locations[pos] = i

        original_path.append((pos, dir))
        i += 1

    else:
        # guard moves off the map, ending patrol
        break


print("Number of unique locations:", len(unique_locations))

################################################################################
# PART 2

# idea I: put obstruction to pos only if the guard visited, because it makes no sense to check for a location which was not encountered in the original path
del unique_locations[start_pos]

# idea II: since we stored the original path, we can fast forward the guard's route to the point where he would hit the obstruction ==> but we need to store the indices of positions first stepped on, hence the memorization in previous part

good_locations = []
for loc in tqdm(unique_locations):

    obstacles.append(loc)

    i = unique_locations[loc]
    new_path = original_path[:i]
    pos = new_path[-1][0]
    dir = new_path[-1][1]

    while True:

        next = (pos[0] + dir[0], pos[1] + dir[1])
        if (0 <= next[0] and next[0] < R) and (0 <= next[1] and next[1] < C):

            # next step is on the map, check if need to turn
            if next in obstacles:
                dir = (dir[1], -dir[0])
            else:
                pos = next

            if (pos, dir) in new_path:
                good_locations.append(loc)
                # guard entered loop with obstacle at loc, reset
                break
            else:
                new_path.append((pos, dir))

        else:
            # guard moves off the map, ending patrol
            # obstacle at loc is not good
            break

    obstacles.remove(loc)

print("Number of possible obstructions:", len(good_locations))
