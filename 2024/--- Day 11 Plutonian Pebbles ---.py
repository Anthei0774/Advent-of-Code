stones_orig = """125 17"""

with open("2024/inputs/11.txt") as f:
    stones_orig = f.read()

stones_orig = stones_orig.split(" ")
stones_orig = list(map(int, stones_orig))

################################################################################
# PART 1

# naive algo for calculating stones, using simply a list and directly operating on it. It is worth making a note that the stones positions are actually irrelevant, so this logic would be wasteful / inefficient for large numbers

stones = stones_orig.copy()
for blink in range(25):

    i = 0
    while i < len(stones):
        st = stones[i]
        s = str(st)
        l = len(s)

        if st == 0:
            stones[i] = 1
            i += 1
        elif l % 2 == 0:
            left = int(s[: l // 2])
            right = int(s[l // 2:])
            stones[i] = left
            stones.insert(i + 1, right)
            i += 2
        else:
            st *= 2024
            stones[i] = st
            i += 1

print("Total number of stones:", len(stones))

################################################################################
# PART 2

# after thinking it through like below, now we are storing stones-numbers only, and that how many of them we have at a given moment

stones = stones_orig.copy()
stones = {s: 1 for s in stones}

for blink in range(75):

    next_stones = {}
    for st in stones:
        s = str(st)
        l = len(s)

        if st == 0:
            if 1 not in next_stones:
                next_stones[1] = stones[st]
            else:
                next_stones[1] += stones[st]

        elif l % 2 == 0:
            left = int(s[: l // 2])

            if left not in next_stones:
                next_stones[left] = stones[st]
            else:
                next_stones[left] += stones[st]

            right = int(s[l // 2:])
            if right not in next_stones:
                next_stones[right] = stones[st]
            else:
                next_stones[right] += stones[st]

        else:
            tmp = st * 2024
            if tmp not in next_stones:
                next_stones[tmp] = stones[st]
            else:
                next_stones[tmp] += stones[st]

    stones = next_stones

print("Total number of stones:", sum(stones.values()))

################################################################################
# THINKITY

# 0
# 1
# 2024
# 20 24
# 2 0 2 4

# 2
# 4048
# 40 48
# 4 0 4 8

# 3
# 6072
# 60 72
# 6 0 7 2

# 4
# 8096
# 80 96
# 8 0 9 6

# 5
# 10120
# 20482880
# 2048 2880
# 20 48 28 80
# 2 0 4 8 2 8 8 0

# 6
# 12144
# 24579456
# 2457 9456
# 24 57 94 56
# 2 4 5 7 9 4 5 6

# 7
# 14168
# 28676032
# 2867 6032
# 28 67 60 32
# 2 8 6 7 6 0 3 2

# 8
# 16112
# 32610688
# 3261 0688
# 32 61 06 88
# 3 2 6 1 0 6 8 8

# 9
# 18216
# 36869184
# 3686 9184
# 36 86 91 84
# 3 6 8 6 9 1 8 4

# Sooo, the stones sequences for single digits are all cyclic, and this means we only need to progress to a state, where these numbers (or some numbers during their cycle) appear.
