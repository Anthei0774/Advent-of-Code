masses = """12
14
1969
100756"""

with open("2019/inputs/1.txt", "r") as f:
    masses = f.read()

masses = masses.split("\n")
masses = list(map(int, masses))

################################################################################
# PART 1

print("Sum of fuel required:", sum(m // 3 - 2 for m in masses))

################################################################################
# PART 2

s = 0
for m in masses:
    while 9 <= m:  # because 8 // 3 - 2 = 0, but 9 // 3 - 2 = 1
        m //= 3
        m -= 2
        s += m

print("Sum of fuel required:", s)
