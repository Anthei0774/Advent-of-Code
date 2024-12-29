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

puzzle = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

with open("2024/inputs/16.txt") as f:
    puzzle = f.read()

puzzle = puzzle.split("\n")
puzzle = [list(row) for row in puzzle]

# process
R = len(puzzle)
C = len(puzzle[0])
all_positions = []
for r in range(R):
    for c in range(C):
        if puzzle[r][c] != "#":
            all_positions.append((r, c))
            if puzzle[r][c] == "S":
                start = (r, c)
            if puzzle[r][c] == "E":
                end = (r, c)

# build a graph with the following structure
# graph = {
#     (pos, dir): {(next_pos, dir): 1, (pos, turn): 1000},
#     (pos, dir): {(next_pos, dir): 1, (pos, turn): 1000},
#     ...,
#     (pos, dir): {(next_pos, dir): 1, (pos, turn): 1000},
# }
graph = {}
for pos in all_positions:
    for dir in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        next = (pos[0] + dir[0], pos[1] + dir[1])

        graph[(pos, dir)] = {}
        if next in all_positions:
            graph[(pos, dir)][(next, dir)] = 1

        left_turn = (-dir[1], dir[0])
        graph[(pos, dir)][(pos, left_turn)] = 1000

        right_turn = (dir[1], -dir[0])
        graph[(pos, dir)][(pos, right_turn)] = 1000

# for node, edges in graph.items():
#     print(node, edges)

################################################################################
# PART 1


def Dijkstra(graph, start):

    all_distances = {node: {"cost": 6 * 10 ** 23, "prev": []}
                     for node in graph}
    all_distances[start]["cost"] = 0

    to_check = [start]

    while to_check != []:
        curr = to_check.pop(0)

        d = all_distances[curr]["cost"]

        for neighbour in graph[curr]:
            if d + graph[curr][neighbour] < all_distances[neighbour]["cost"]:
                all_distances[neighbour]["cost"] = d + graph[curr][neighbour]
                all_distances[neighbour]["prev"] = [curr]
                to_check.append(neighbour)
            elif d + graph[curr][neighbour] == all_distances[neighbour]["cost"]:
                all_distances[neighbour]["prev"].append(curr)

    return all_distances


all_distances = Dijkstra(graph, (start, (0, 1)))
m = min(dist["cost"]
        for state, dist in all_distances.items() if state[0] == end)
print("Score:", m)

# for state, dist in all_distances.items():
#     print(state, dist)

for state in all_distances:
    if state[0] == end and all_distances[state]["cost"] == m:
        break

all_tiles = [[state]]

while True:
    new_tiles = []

    for t in all_tiles[-1]:

        for tt in all_distances[t]["prev"]:
            if tt not in new_tiles:
                new_tiles.append(tt)

    if new_tiles == []:
        break
    else:
        all_tiles.append(new_tiles)

s = len(set(tt[0] for t in all_tiles for tt in t))
print(s)
