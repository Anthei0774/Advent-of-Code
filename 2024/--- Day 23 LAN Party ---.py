from itertools import combinations
from tqdm import tqdm

puzzle = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""

with open("2024/inputs/23.txt") as f:
    puzzle = f.read()

puzzle = puzzle.split("\n")
puzzle = [line.split("-") for line in puzzle]
puzzle = [tuple(line) for line in puzzle]
# print("Puzzle:", puzzle)

################################################################################
# PART 1

# build graph from puzzle
graph = {}
for edge in puzzle:

    if edge[0] not in graph:
        graph[edge[0]] = [edge[1]]
    elif edge[1] not in graph[edge[0]]:
        graph[edge[0]].append(edge[1])

    if edge[1] not in graph:
        graph[edge[1]] = [edge[0]]
    elif edge[0] not in graph[edge[1]]:
        graph[edge[1]].append(edge[0])

# sort nodes and connections alphabetically
graph = {node: sorted(graph[node]) for node in sorted(graph)}

N = len(graph)
print("Graph size:", N)

# for node, edges in graph.items():
#     print(node, edges)

# check for triangles
C = 0
for c in combinations(list(graph), 3):
    (u, v, w) = c
    if (v in graph[u]) and (w in graph[v]) and (u in graph[w]):
        C += ("t" in [u[0], v[0], w[0]])

print("Part 1 answer:", C)
