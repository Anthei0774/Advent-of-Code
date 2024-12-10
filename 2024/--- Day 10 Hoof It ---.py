height_map = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

with open("2024/inputs/10.txt", "r") as f:
    height_map = f.read()

height_map = height_map.split("\n")
height_map = [list(line) for line in height_map]
height_map = [[h if h.isnumeric() else -1 for h in line]
              for line in height_map]
height_map = [list(map(int, line)) for line in height_map]

R = len(height_map)
C = len(height_map[0])

################################################################################
# PART 1

# map from trailhead starting pos to number of endpoints
trailheads = {(r, c): 0 for r in range(R)
              for c in range(C) if height_map[r][c] == 0}

# implementing a simple BFS (Breadth-First-Search)
for th in trailheads:

    # init layer-0 as the starting pos. Layer-1 will contain immediate neighbours, layer-2 will contain the second ones, and so on...
    layers = {0: [th]}

    for l in range(1, 10):
        layers[l] = []

        # iterate through the previous layer nodes
        for (r, c) in layers[l - 1]:
            neighbours = [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]
            neighbours = [n for n in neighbours if (
                0 <= n[0] and n[0] < R) and (0 <= n[1] and n[1] < C)]
            neighbours = [n for n in neighbours if height_map[n[0]]
                          [n[1]] == height_map[r][c] + 1]

            # if found a valid neighbour for a layer node, add it to the next one
            for n in neighbours:
                if n not in layers[l]:
                    layers[l].append(n)

    if 9 in layers:
        trailheads[th] += len(layers[9])

print("Sum of scores:", sum(trailheads.values()))

################################################################################
# PART 2

# all paths currently under examination
paths = [[(r, c)] for r in range(R) for c in range(C) if height_map[r][c] == 0]

# all unique paths stored as a list of 10-length-lists, initially empty
completed_paths = []

# loop until no more paths to process
while paths != []:

    # take last point of path, and check for extensions
    p = paths.pop(0)
    (r, c) = p[-1]

    neighbours = [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]
    neighbours = [n for n in neighbours if (
        0 <= n[0] and n[0] < R) and (0 <= n[1] and n[1] < C)]
    neighbours = [n for n in neighbours if height_map[n[0]]
                  [n[1]] == height_map[r][c] + 1]

    # if any extensions, then check for completion or add back to examined ones
    for n in neighbours:
        tmp = p.copy()
        tmp.append(n)
        if len(tmp) == 10:
            completed_paths.append(tmp)
        else:
            paths.append(tmp)

print("Sum of ratings:", len(completed_paths))
