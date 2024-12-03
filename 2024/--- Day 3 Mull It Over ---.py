################################################################################
# PART 1

import re

muls = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

with open("2024/inputs/3.txt", "r") as f:
    muls = f.read()

muls = re.findall("mul\(\d+,\d+\)", muls)
muls = [m[4: -1].split(",") for m in muls]
muls = [tuple(map(int, m)) for m in muls]

s = sum(m[0] * m[1] for m in muls)
print("Sum of multiplications:", s)

################################################################################
# PART 2

muls = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

with open("2024/inputs/3.txt", "r") as f:
    muls = f.read()

s = 0

i = 0
ii = 0
muls_enabled = True
while i < len(muls):

    # if muls are not enabled, then search for the next enabler, and jump with the index
    if not muls_enabled:
        i = muls.find("do()", ii)
        muls_enabled = True

    # if enabled, race with not-enabler and next potential mul block
    ii = muls.find("don't()", i)
    i = muls.find("mul(", i)
    if ii != -1 and ii < i:
        muls_enabled = False
        continue
    if i == -1:
        break

    # mul block starts
    try:
        # jump with 4, then start adding the digits to first number
        n1 = ""
        i += 4
        while i < len(muls) and muls[i].isnumeric():
            n1 += muls[i]
            i += 1

        # if invalid mul block, step out
        assert muls[i] == ","
        i += 1

        # adding digits to second number
        n2 = ""
        while i < len(muls) and muls[i].isnumeric():
            n2 += muls[i]
            i += 1

        # invalid block, step out
        assert muls[i] == ")"

        # valid mul block, increment sum
        s += int(n1) * int(n2)
        # print(i, n1, n2, s)

    except AssertionError:
        continue

print("Sum of multiplications:", s)
