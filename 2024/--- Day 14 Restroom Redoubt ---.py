robots_orig = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""
R = 7
C = 11

with open("2024/inputs/14.txt") as f:
    robots_orig = f.read()
    R = 103
    C = 101

# process data
robots_orig = robots_orig.split("\n")
for i, r in enumerate(robots_orig):
    r = r.split(" ")
    r[0] = r[0][2:].split(",")
    r[0] = tuple(map(int, r[0]))
    r[1] = r[1][2:].split(",")
    r[1] = tuple(map(int, r[1]))
    r = {"p": r[0], "v": r[1]}
    robots_orig[i] = r

################################################################################
# PART 1

robots = [r.copy() for r in robots_orig]

# loop with the robots moving around
for cycle in range(100):
    for r in robots:
        r["p"] = (r["p"][0] + r["v"][0], r["p"][1] + r["v"][1])
        r["p"] = (r["p"][0] % C, r["p"][1] % R)

# check each quadrant
quadrants = [0 for q in range(4)]
for r in robots:
    if (r["p"][0] < C // 2) and (r["p"][1] < R // 2):
        quadrants[0] += 1
    elif (C // 2 < r["p"][0]) and (r["p"][1] < R // 2):
        quadrants[1] += 1
    if (r["p"][0] < C // 2) and (R // 2 < r["p"][1]):
        quadrants[2] += 1
    elif (C // 2 < r["p"][0]) and (R // 2 < r["p"][1]):
        quadrants[3] += 1

print("Product of quadrants' safety factor:",
      quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])

################################################################################
# PART 2

# reset
robots = [r.copy() for r in robots_orig]

# in each cycle, create a snapshot on the robots' positions
all_images = []
while True:
    image = [["." for c in range(C)] for r in range(R)]

    for r in robots:
        r["p"] = (r["p"][0] + r["v"][0], r["p"][1] + r["v"][1])
        r["p"] = (r["p"][0] % C, r["p"][1] % R)

        image[r["p"][1]][r["p"][0]] = "#"

    image = ["".join(row) for row in image]
    image = "\n".join(image)

    # if encountering the same image, then we have made a complete cycle, aborting
    if image not in all_images:
        all_images.append(image)
    else:
        break

print("Number of unique images:", len(all_images))

# checked the text file manually, but only found the a christmas tree. Checked on Reddit, and everybody else is posting a christmas tree... Re-reading part 2 like 10 times until I realize that we are looking for an "easter egg", which is a christmas tree... :')

# with open("2024/xmas_tree.txt", mode="w+") as f:
#     f.write("")
# with open("2024/xmas_tree.txt", mode="a") as f:
#     for i in range(len(all_images)):
#         f.write(str(i + 1) + "\n")
#         f.write(all_images[i] + "\n")

print("Answer: 8159")
