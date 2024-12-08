antennas = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

with open("2024/inputs/8.txt") as f:
    antennas = f.read()

antennas = antennas.split("\n")
antennas = [list(row) for row in antennas]

R = len(antennas)
C = len(antennas[0])

for r in range(R):
    for c in range(C):
        if antennas[r][c] != ".":
            antennas.append((r, c, antennas[r][c]))

antennas = [{"pos": a[:2], "freq": a[2]} for a in antennas if type(a) == tuple]

################################################################################
# PART 1

n = len(antennas)

antinodes = []
for i in range(n):
    ai = antennas[i]

    for j in range(i + 1, n):
        aj = antennas[j]

        if ai["freq"] == aj["freq"]:

            # vector pointing from ai to aj
            d = (aj["pos"][0] - ai["pos"][0], aj["pos"][1] - ai["pos"][1])

            # going left / above
            tmp = (ai["pos"][0] - d[0], ai["pos"][1] - d[1])
            if (0 <= tmp[0] and tmp[0] < R) and (0 <= tmp[1] and tmp[1] < C):
                if tmp not in antinodes:
                    antinodes.append(tmp)

            # going right / below
            tmp = (aj["pos"][0] + d[0], aj["pos"][1] + d[1])
            if (0 <= tmp[0] and tmp[0] < R) and (0 <= tmp[1] and tmp[1] < C):
                if tmp not in antinodes:
                    antinodes.append(tmp)

print("Number of unique locations:", len(antinodes))

################################################################################
# PART 2

antinodes = []
for i in range(n):
    ai = antennas[i]

    for j in range(i + 1, n):
        aj = antennas[j]

        if ai["freq"] == aj["freq"]:

            # antennas itselves are now also antinodes
            if ai["pos"] not in antinodes:
                antinodes.append(ai["pos"])
            if aj["pos"] not in antinodes:
                antinodes.append(aj["pos"])

            # vector pointing from ai to aj
            d = (aj["pos"][0] - ai["pos"][0], aj["pos"][1] - ai["pos"][1])

            # going left / above
            i = 1
            while True:
                tmp = (ai["pos"][0] - i * d[0], ai["pos"][1] - i * d[1])
                if (0 <= tmp[0] and tmp[0] < R) and (0 <= tmp[1] and tmp[1] < C):
                    if tmp not in antinodes:
                        antinodes.append(tmp)
                    i += 1
                else:
                    break

            # going right / below
            i = 1
            while True:
                tmp = (aj["pos"][0] + i * d[0], aj["pos"][1] + i * d[1])
                if (0 <= tmp[0] and tmp[0] < R) and (0 <= tmp[1] and tmp[1] < C):
                    if tmp not in antinodes:
                        antinodes.append(tmp)
                    i += 1
                else:
                    break

print("Number of unique locations:", len(antinodes))
