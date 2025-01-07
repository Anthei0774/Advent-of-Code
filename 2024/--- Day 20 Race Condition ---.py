puzzle = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""

with open("2024/inputs/20.txt") as file:
    puzzle = file.read()

puzzle = puzzle.split("\n")
puzzle = [list(line) for line in puzzle]

racetrack_graph = {}
walls_graph = {}

R = len(puzzle)
C = len(puzzle[0])

for r in range(R):
    for c in range(C):

        if puzzle[r][c] == "S":
            start = (r, c)
        if puzzle[r][c] == "E":
            end = (r, c)

        if puzzle[r][c] == "#":
            walls_graph[(r, c)] = []
        else:
            racetrack_graph[(r, c)] = {}


for pos in racetrack_graph:
    for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        next_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if next_pos in racetrack_graph:
            racetrack_graph[pos][next_pos] = 1

for pos in walls_graph:
    for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        next_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if next_pos in racetrack_graph:
            walls_graph[pos].append(next_pos)

################################################################################
# PART 1
################################################################################


def Dijkstra(graph, start):

    dist = {node: float("inf") for node in graph}
    dist[start] = 0

    unvisited = set(graph)
    while unvisited:
        current = min(unvisited, key=lambda node: dist[node])
        unvisited.remove(current)

        for neighbor in graph[current]:
            alt = dist[current] + graph[current][neighbor]
            if alt < dist[neighbor]:
                dist[neighbor] = alt

    return dist


distances = Dijkstra(racetrack_graph, end)

cheats = {}
for wall in walls_graph:

    if len(walls_graph[wall]) in [2, 3]:
        # print(walls_graph[wall])
        tmp = {pos: distances[pos] for pos in walls_graph[wall]}
        w0 = max(tmp, key=tmp.get)
        w1 = min(tmp, key=tmp.get)
        del tmp
    else:
        continue

    assert distances[w0] >= distances[w1] + 2
    # print(w0, w1, distances[w0], distances[w1])

    c = distances[w0] - distances[w1] - 2
    if c not in cheats:
        cheats[c] = [wall]
    else:
        cheats[c].append(wall)

cheats = {c: cheats[c] for c in sorted(cheats)}

# for c in cheats:
#     print(c, cheats[c])

print(sum(len(cheats[c]) for c in cheats if c >= 100))
