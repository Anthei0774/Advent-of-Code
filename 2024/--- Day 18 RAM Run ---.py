positions = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

R = 7
C = 7
cut = 12

with open("2024/inputs/18.txt") as f:
    positions = f.read()
    R = 71
    C = 71
    cut = 1024

positions = positions.split("\n")
positions = [p.split(",") for p in positions]
positions = [tuple(map(int, p)) for p in positions]
positions = positions[:cut]

################################################################################
# PART 1

graph = {(c, r): [] for c in range(C)
         for r in range(R) if (c, r) not in positions}

for pos in graph:
    for dir in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        next = (pos[0] + dir[0], pos[1] + dir[1])
        if next in graph:
            graph[pos].append(next)

tmp = """"""
for c in range(C):
    for r in range(R):
        if (c, r) in graph:
            tmp += "."
        else:
            tmp += "#"
    tmp += "\n"
print(tmp)

start = (0, 0)
layers = [[start]]
checked = []
while True:

    current_layer = layers[-1]
    next_layer = []

    for node in current_layer:
        if node == (R - 1, C - 1):
            print(len(layers) - 1)
        for neighbour in graph[node]:
            if neighbour not in checked and neighbour not in next_layer:
                next_layer.append(neighbour)
            checked.append(node)

    if next_layer == []:
        break

    layers.append(next_layer)
