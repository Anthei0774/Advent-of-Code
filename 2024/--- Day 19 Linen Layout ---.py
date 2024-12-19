from tqdm import tqdm

puzzle = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

with open("2024/inputs/19.txt") as f:
    puzzle = f.read()

puzzle = puzzle.split("\n")
patterns = puzzle[0].split(", ")
designs = puzzle[2:]
designs = {d: False for d in designs}

##################################################################
# PART 1

# recursive function for slicing a prefix-pattern off from the given design. Early abort of searching with return-True in case of a solution found.


def check_design(d):
    global patterns

    # if design is empty, then it the right patterns were sliced off
    if d == "":
        return True

    # if not empty, then try to slice off a matching pattern, continue searching on the shortened one
    for p in patterns:
        level = len(p)
        if (level <= len(d)) and (p == d[:level]):
            if check_design(d[level:]):
                return True

    return False


# also saving if a design can be completed (for part 2)
C = 0
for d in designs:
    designs[d] = check_design(d)
    C += designs[d]
print("Possible designs:", C)

##################################################################
# PART 2

# same prefix slicing logic, but with different data structures

C = 0
for d in tqdm(designs):

    # only check those designs which could be completed in part 1
    if not designs[d]:
        continue

    # level-0, original design
    # level-1, slices taken off from level 0, duplicates counted
    # level-2, slices taken off from level 1, also with duplicates counted
    levels = [{d: 1}]

    # full algo until no more levels can be added
    while True:

        # iterate through the last level deisgns
        level = levels[-1]
        next_level = {}
        for level_d in level:

            if level_d == "":
                continue

            # for a given design, check for matching prefix-patterns. If a matching pattern exists, then add to next layer
            for p in patterns:
                l = len(p)
                if (l <= len(level_d)) and (p == level_d[:l]):

                    tmp = level_d[l:]
                    if tmp in next_level:
                        next_level[tmp] += level[level_d]
                    else:
                        next_level[tmp] = level[level_d]

        # if no new patterns were generated, step out, this design's checking is completed
        if next_level == {}:
            break
        else:
            # if a "" was inserted in this iteration, then increase scoring
            if "" in next_level:
                C += next_level[""]
            levels.append(next_level)

print("Sum of different ways for desgins:", C)
