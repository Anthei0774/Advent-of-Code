locations = """3   4
4   3
2   5
1   3
3   9
3   3"""

with open("2024/inputs/1.txt") as f:
    locations = f.read()

################################################################################
# PART 1

locations = locations.split("\n")
N = len(locations)

# transform into [l1, l2], where l1, l2 are sorted lists
locations = [l.split("   ") for l in locations]
locations = [tuple(map(int, l)) for l in locations]
locations = [[locations[j][i] for j in range(N)] for i in range(2)]
locations = [sorted(l) for l in locations]

print("Total distance:", sum(
    abs(locations[0][i] - locations[1][i]) for i in range(N)))

################################################################################
# PART 2

print("Similarity score:", sum(locations[1].count(
    locations[0][i]) * locations[0][i] for i in range(N)))
