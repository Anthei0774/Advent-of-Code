################################################################################
# PART 1

lines = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

with open("2023/inputs/1.txt", "r") as f:
    lines = f.read()

lines = lines.split("\n")

s = 0

for l in lines:

    # forwards
    i = 0
    while not l[i].isnumeric():
        i += 1

    # backwards
    j = len(l) - 1
    while not l[j].isnumeric():
        j -= 1

    s += 10 * int(l[i]) + int(l[j])

print("Sum of calibration values:", s)

################################################################################
# PART 2

lines = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

with open("2023/inputs/1.txt", "r") as f:
    lines = f.read()

lines = lines.split("\n")

words = ["one", "two", "three", "four",
         "five", "six", "seven", "eight", "nine"]

s = 0

for l in lines:

    # forwards
    findings = [{"index": l.find(w), "value": words.index(w) + 1}
                for w in words if l.find(w) != -1]
    if findings != []:
        findings = sorted(findings, key=lambda f: f["index"])
        findings = findings[0]
    else:
        findings = {"index": len(l)}

    i = 0
    while i < len(l):
        if not l[i].isnumeric():
            i += 1
        else:
            break

    left = int(l[i]) if i < findings["index"] else findings["value"]

    # backwards
    findings = [{"index": l.rfind(w), "value": words.index(w) + 1}
                for w in words if l.rfind(w) != -1]
    if findings != []:
        findings = sorted(findings, key=lambda f: f["index"])
        findings = findings[-1]
    else:
        findings = {"index": -1}

    j = len(l) - 1
    while 0 <= j:
        if not l[j].isnumeric():
            j -= 1
        else:
            break

    right = int(l[j]) if findings["index"] < j else findings["value"]

    # sum
    s += left * 10 + right

print("Sum of calibration values:", s)
