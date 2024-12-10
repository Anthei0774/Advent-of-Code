################################################################################
# PART 1

reports = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

with open("2024/inputs/2.txt") as f:
    reports = f.read()

reports = reports.split("\n")
reports = [r.split(" ") for r in reports]
reports = [list(map(int, r)) for r in reports]

c = 0
for r in reports:

    diffs = [r[i + 1] - r[i] for i in range(len(r) - 1)]

    all_increasing = all(d > 0 for d in diffs)
    all_decreasing = all(d < 0 for d in diffs)
    steep_ok = all(1 <= abs(d) and abs(d) <= 3 for d in diffs)

    c += ((all_increasing or all_decreasing) and steep_ok)

print("Number of safe reports:", c)

################################################################################
# PART 2

c = 0
for r in reports:

    diffs = [r[i + 1] - r[i] for i in range(len(r) - 1)]
    all_increasing = all(d > 0 for d in diffs)
    all_decreasing = all(d < 0 for d in diffs)
    steep_ok = all(1 <= abs(d) and abs(d) <= 3 for d in diffs)

    if ((all_increasing or all_decreasing) and steep_ok):
        c += 1
    else:

        # if not ok, then brute force search: take copies of the levels and remove one until the good one is found, else indeed unsafe report
        j = 0
        while j < len(r):
            rr = r.copy()
            rr.pop(j)

            diffs = [rr[i + 1] - rr[i] for i in range(len(rr) - 1)]
            all_increasing = all(d > 0 for d in diffs)
            all_decreasing = all(d < 0 for d in diffs)
            steep_ok = all(1 <= abs(d) and abs(d) <= 3 for d in diffs)

            if ((all_increasing or all_decreasing) and steep_ok):
                c += 1
                break
            else:
                j += 1

print("Number of safe reports:", c)
