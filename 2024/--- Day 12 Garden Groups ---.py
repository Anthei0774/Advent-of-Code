garden = """AAAA
BBCD
BBCC
EEEC"""

garden = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""

garden = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""

# garden = """RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE"""

# with open("2024/inputs/12.txt") as f:
#     garden = f.read()

garden = garden.split("\n")
garden = [list(row) for row in garden]
R = len(garden)
C = len(garden[0])
garden = {(r, c): garden[r][c] for r in range(R) for c in range(C)}

################################################################################
# PART 1

plots_to_check = list(garden)
regions = []

while plots_to_check != []:
    p = plots_to_check.pop(0)

    # open a new region for p, and initialize a container with its neighbours. These neighbours_to_check container will contain those positions whose pots are candidates for the p-region
    new_region = [p]
    (r, c) = p
    neighbours_to_check = [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]
    while neighbours_to_check != []:
        n = neighbours_to_check.pop(0)

        # if neighbour is not the map or not matching with p-region, discard it
        if (n not in garden) or (garden[p] != garden[n]):
            continue

        # otherwise: this neighbour belongs to p-region, and thus no need to start a new region for it later, remove for checklist
        new_region.append(n)
        plots_to_check.remove(n)

        # for this neighbours' neighbours, add them all to this p-region's container, since they are candidate
        (nr, nc) = n
        neighbours_neighbours = [
            (nr - 1, nc), (nr, nc - 1), (nr, nc + 1), (nr + 1, nc)]
        for nn in neighbours_neighbours:
            if (nn not in neighbours_to_check) and (nn not in new_region):
                neighbours_to_check.append(nn)

    regions.append({"id": garden[p], "pots": new_region})

# step 2: iterate through all regions and calculate their area and perimeter
S = 0
for region in regions:
    A = len(region["pots"])

    # init the perimeter as 4 times the number of pots. And for each coverage subtract 1. Since we do this for, we will subtract two for a pair with neighbouring sides
    P = len(region["pots"]) * 4
    for p in region["pots"]:
        (r, c) = p
        for n in [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]:
            if n in region["pots"]:
                P -= 1

    # print("Area:", A, "Perimeter:", P)
    S += A * P

print("Total price of fencing:", S)

################################################################################
# PART 2

S = 0

for region in regions:

    print(region)

    # calculate the boundary of region, we are taking 8-adjacency, counting diagonals as well
    boundary_points = []
    for pot in region["pots"]:
        (r, c) = pot
        for n in [
            (r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
            (r, c - 1),     (r, c),     (r, c + 1),
            (r + 1, c - 1), (r + 1, c), (r + 1, c + 1),
        ]:
            if (n not in region["pots"]) and (n not in boundary_points):
                boundary_points.append(n)

    boundary_points = sorted(
        sorted(boundary_points, key=lambda p: p[1]), key=lambda p: p[0])

    #
    boundary_connected_components = []
    while boundary_points != []:
        (r, c) = boundary_points.pop(0)

        new_component = True
        for components in boundary_connected_components:
            if ((r - 1, c) in components) or \
               ((r, c - 1) in components) or \
               ((r, c + 1) in components) or \
               ((r + 1, c) in components):
                components.append((r, c))
                new_component = False
                break

        if new_component:
            boundary_connected_components.append([(r, c)])

    first_run = True
    for component in boundary_connected_components:

        if len(component) == 1:
            sides += 4
            continue

        sides = 1

        # start from left-most top and travel around / inside the region. We basically implement the algorithm that our right hand is on the fence always. On the first run, we start moving to the right, and hence will circle the region. On subsequent runs, we start moving down always, right hand is still on the wall. Each turn indicates a new side.
        startend = component[0]
        dir = (0, 1) if first_run else (1, 0)
        turn_right = False if first_run else True
        pos = startend
        while True:
            print(pos, dir)
            next = (pos[0] + dir[0], pos[1] + dir[1])

            # if the next step is the starting point, we break out, since have gone a full circle
            if next == startend:
                break

            # when turning right at any time (even right at the beginning), it is possible to turn again, going backwards essentially. We can avoid this with a simple bool switch, which refers to the behavior that we actually want to turn right
            if turn_right:

                # if possible turning right, then turn right
                right_next = (pos[0] + dir[1], pos[1] - dir[0])
                if right_next in component:
                    dir = (dir[1], -dir[0])
                    sides += 1
                    turn_right = False
                    continue

            else:
                turn_right = True

            # if would hit a wall, turn left
            if next in region["pots"]:
                dir = (-dir[1], dir[0])
                sides += 1
                continue

            # at this point:
            # 1) not the end of path
            # 2) not hitting a wall (turning left)
            # 3) not possible to turn right
            # ==> proceed forward
            pos = next

        print(sides)
        first_run = False
        print()

    S += len(region["pots"]) * sides

print(S)
