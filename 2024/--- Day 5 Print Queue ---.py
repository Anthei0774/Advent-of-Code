inputs = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

with open("2024/inputs/5.txt") as f:
    inputs = f.read()

# take orderings, process and sort into ascending order
ordering_rules = inputs.split("\n\n")[0]
ordering_rules = ordering_rules.split("\n")
ordering_rules = [r.split("|") for r in ordering_rules]
ordering_rules = [tuple(map(int, r)) for r in ordering_rules]
ordering_rules = sorted(
    sorted(ordering_rules, key=lambda r: r[1]), key=lambda r: r[0])

# process manuals
manual_updates = inputs.split("\n\n")[1]
manual_updates = manual_updates.split("\n")
manual_updates = [u.split(",") for u in manual_updates]
manual_updates = [list(map(int, u)) for u in manual_updates]
manual_updates = [{"pages": u} for u in manual_updates]

################################################################################
# PART 1

s = 0

for u in manual_updates:
    correct = True

    l = len(u["pages"])
    assert l % 2 == 1

    # check for out-of-order pages
    for i in range(l):
        for j in range(i + 1, l):
            if (u["pages"][j], u["pages"][i]) in ordering_rules:
                correct = False
                break

        if not correct:
            break

    # increment sum with middle page number
    if correct:
        s += u["pages"][l // 2]

    u["correct"] = correct

print("Sum of middle numbers on correct pages:", s)

################################################################################
# PART 2

s = 0

for u in manual_updates:
    if not u["correct"]:

        l = len(u["pages"])
        pages = u["pages"].copy()

        # a naive sorting algorithm: if we find some violating pages, then swap those.
        i = 0
        while i < l:
            reset = False
            j = i + 1
            while j < l:
                if (pages[j], pages[i]) in ordering_rules:
                    tmp = pages[i]
                    pages[i] = pages[j]
                    pages[j] = tmp
                    reset = True
                    break
                else:
                    j += 1
            if reset:
                i = 0
            else:
                i += 1

        # slow, but at least it's correct... :')

        # print("Corrected order:", pages)
        s += pages[l // 2]

print("Sum of middle numbers on corrected pages:", s)
