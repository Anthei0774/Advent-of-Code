word_search = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

# with open("2024/inputs/4.txt", "r") as f:
#     word_search = f.read()

word_search = word_search.split("\n")
word_search = [list(line) for line in word_search]

################################################################################
# PART 1

R = len(word_search)
C = len(word_search[0])
total = 0

for r in range(R):
    for c in range(C):

        # horizontal from left to right
        if c < C - 3:
            total += ((word_search[r][c] + word_search[r][c + 1] +
                      word_search[r][c + 2] + word_search[r][c + 3]) == "XMAS")
        # horizontal from right to left
        if 3 <= c:
            total += ((word_search[r][c] + word_search[r][c - 1] +
                      word_search[r][c - 2] + word_search[r][c - 3]) == "XMAS")
        # vertical from top to bottom
        if r < R - 3:
            total += ((word_search[r][c] + word_search[r + 1][c] +
                      word_search[r + 2][c] + word_search[r + 3][c]) == "XMAS")
        # vertical from bottom to top
        if 3 <= r:
            total += ((word_search[r][c] + word_search[r - 1][c] +
                      word_search[r - 2][c] + word_search[r - 3][c]) == "XMAS")
        # diagonal from top-left to bottom-right
        if (r < R - 3) and (c < C - 3):
            total += ((word_search[r][c] + word_search[r + 1][c + 1] +
                      word_search[r + 2][c + 2] + word_search[r + 3][c + 3]) == "XMAS")
        # diagonal from bottom-left to top-right
        if (3 <= r) and (c < C - 3):
            total += ((word_search[r][c] + word_search[r - 1][c + 1] +
                      word_search[r - 2][c + 2] + word_search[r - 3][c + 3]) == "XMAS")
        # diagonal from bottom-right to top-left
        if (3 <= r) and (3 <= c):
            total += ((word_search[r][c] + word_search[r - 1][c - 1] +
                      word_search[r - 2][c - 2] + word_search[r - 3][c - 3]) == "XMAS")
        # diagonal from top-right to bottom-left
        if (r < R - 3) and (3 <= c):
            total += ((word_search[r][c] + word_search[r + 1][c - 1] +
                      word_search[r + 2][c - 2] + word_search[r + 3][c - 3]) == "XMAS")

print("XMAS occurance:", total)

################################################################################
# PART 2

total = 0

for r in range(1, R - 1):
    for c in range(1, C - 1):

        # M.S   M.M   S.M   S.S
        # .A.   .A.   .A.   .A.
        # M.S   S.S   S.M   M.M
        w = word_search[r - 1][c - 1] + word_search[r - 1][c + 1] + \
            word_search[r][c] + word_search[r + 1][c - 1] + \
            word_search[r + 1][c + 1]

        total += (w in ["MSAMS", "MMASS", "SMASM", "SSAMM"])

print("XMAS occurance:", total)
