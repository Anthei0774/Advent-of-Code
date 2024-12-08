schematic = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

with open("2023/inputs/3.txt") as f:
    schematic = f.read()

schematic = schematic.split("\n")
schematic = [list(line) for line in schematic]
schematic

# apply a 1-wide frame of "."
l = len(schematic[0])
schematic.insert(0, ["."] * l)
schematic.append(["."] * l)
for i, line in enumerate(schematic):
    line.insert(0, ".")
    line.append(".")
    schematic[i] = line

################################################################################
# PART 1

R = len(schematic)
C = len(schematic[0])

S = 0

r = 1
while r < R - 1:

    c = 1
    while c < C - 1:

        l = 0
        while schematic[r][c + l].isnumeric():
            l += 1

        if l != 0:
            # create number
            n = schematic[r][c: c + l]
            n = "".join(n)
            n = int(n)

            # create window around number
            window = schematic[r - 1][c - 1: c + l + 1]
            window.append(schematic[r][c - 1])
            window.append(schematic[r][c + l])
            window += schematic[r + 1][c - 1: c + l + 1]
            # l + 2 up and down, plus 1-1 on sides
            assert len(window) == 2 * (l + 2) + 2

            # only interested in distinct characters
            window = set(window)
            if window != {"."}:
                S += n

            # step by number length
            c += l
        else:
            c += 1

    # one row down
    r += 1

print("Sum of gear ratios:", S)

################################################################################
# PART 2

S = 0

r = 1
while r < R - 1:

    c = 1
    while c < C - 1:

        if schematic[r][c] == "*":

            # ABOVE
            above = schematic[r - 1][c - 1: c + 2]
            if above[0].isnumeric():
                l = 2
                while schematic[r - 1][c - l].isnumeric():
                    above.insert(0, schematic[r - 1][c - l])
                    l += 1

            if above[-1].isnumeric():
                l = 2
                while schematic[r - 1][c + l].isnumeric():
                    above.append(schematic[r - 1][c + l])
                    l += 1

            # above should be either of following three cases:
            # 1. 123..
            # 2. ..123
            # 2. 123.123
            above = "".join(above)
            above = above.strip(".")
            above = above.split(".")
            above = [int(number) for number in above if number.isnumeric()]

            assert len(above) in [0, 1, 2]
            # print("Above:", above)

            # LEFT
            left = schematic[r][c - 1]
            if left.isnumeric():
                l = 2
                while schematic[r][c - l].isnumeric():
                    left = schematic[r][c - l] + left
                    l += 1

            # left should be either:
            # 1. .
            # 2. 123
            left = left.strip(".")
            left = left.split(".")
            left = [int(number) for number in left if number.isnumeric()]

            assert len(left) in [0, 1]
            # print("Left:", left)

            # RIGHT
            right = schematic[r][c + 1]
            if right.isnumeric():
                l = 2
                while schematic[r][c + l].isnumeric():
                    right += schematic[r][c + l]
                    l += 1

            # right should be either:
            # 1. .
            # 2. 123
            right = right.strip(".")
            right = right.split(".")
            right = [int(number) for number in right if number.isnumeric()]

            assert len(right) in [0, 1]
            # print("Right:", right)

            # BELOW
            below = schematic[r + 1][c - 1: c + 2]
            if below[0].isnumeric():
                l = 2
                while schematic[r + 1][c - l].isnumeric():
                    below.insert(0, schematic[r + 1][c - l])
                    l += 1

            if below[-1].isnumeric():
                l = 2
                while schematic[r + 1][c + l].isnumeric():
                    below.append(schematic[r + 1][c + l])
                    l += 1

            # below should be either of following three cases:
            # 1. 123..
            # 2. ..123
            # 2. 123.123
            below = "".join(below)
            below = below.strip(".")
            below = below.split(".")
            below = [int(number) for number in below if number.isnumeric()]

            assert len(below) in [0, 1, 2]
            # print("Below:", below)

            # TOTAL
            total = above + left + right + below
            # print("Total:", total)

            if len(total) == 2:
                p = 1
                for number in total:
                    p *= number
                S += p

        c += 1

    # one row down
    r += 1

print("Sum of gear ratios:", S)
