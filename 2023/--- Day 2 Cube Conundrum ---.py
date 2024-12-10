games = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

with open("2023/inputs/2.txt") as f:
    games = f.read()

games = games.replace(" ", "").split("\n")

for i, g in enumerate(games):

    g = g.replace("blue", "B").replace("green", "G").replace("red")
    g = g[g.find(":") + 1:]

    g = g.split(";")
    g = [set_of_cubes.split(",") for set_of_cubes in g]
    # sort a set of group into BGR (alphabetical order)
    g = [sorted(set_of_cubes, key=lambda c: c[-1]) for set_of_cubes in g]

    for j, set_of_cubes in enumerate(g):

        assert len(set_of_cubes) <= 3

        colors = [c[-1] for c in set_of_cubes]
        if "B" not in colors:
            set_of_cubes.insert(0, "0B")
        if "G" not in colors:
            set_of_cubes.insert(1, "0G")
        if "R" not in colors:
            set_of_cubes.append("0R")

        set_of_cubes = [int(c[:-1]) for c in set_of_cubes]
        g[j] = set_of_cubes

    games[i] = g

################################################################################
# PART 1

BGR = (14, 13, 12)  # only 12 red cubes, 13 green cubes, and 14 blue cubes

S = 0
for i, g in enumerate(games):
    possible = all((set_of_cubes[0] <= BGR[0]) and (set_of_cubes[1] <= BGR[1]) and (
        set_of_cubes[2] <= BGR[2]) for set_of_cubes in g)
    if possible:
        S += (i + 1)

print("Sum of games' ids:", S)

################################################################################
# PART 2

S = 0
for g in games:

    B = max(set_of_cubes[0] for set_of_cubes in g)
    G = max(set_of_cubes[1] for set_of_cubes in g)
    R = max(set_of_cubes[2] for set_of_cubes in g)

    S += (B * G * R)

print("Sum of power sets:", S)
