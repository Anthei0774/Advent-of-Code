scratchcards = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

with open("2023/inputs/4.txt") as f:
    scratchcards = f.read()

scratchcards = scratchcards.split("\n")

for i, card in enumerate(scratchcards):

    card = card.split(": ")[1]
    card = card.split(" | ")

    # winning numbers
    card[0] = card[0].split(" ")
    card[0] = [num for num in card[0] if num != ""]
    card[0] = list(map(int, card[0]))
    card[0] = sorted(card[0])

    # numbers we have
    card[1] = card[1].split(" ")
    card[1] = [num for num in card[1] if num != ""]
    card[1] = list(map(int, card[1]))
    card[1] = sorted(card[1])

    card = {"winning": card[0], "numbers": card[1]}
    scratchcards[i] = card

################################################################################
# PART 1

S = 0
for card in scratchcards:
    p = sum([w in card["numbers"] for w in card["winning"]])
    if p >= 2:
        p = 2 ** (p - 1)
    S += p

print("Total points:", S)

################################################################################
# PART 2

for card in scratchcards:
    card["pieces"] = 1

for i, card in enumerate(scratchcards):
    p = sum([w in card["numbers"] for w in card["winning"]])

    # add copies
    for j in range(1, p + 1):
        if i + j < len(scratchcards):
            scratchcards[i + j]["pieces"] += card["pieces"]

# sum up the original + copies
S = sum(card["pieces"] for card in scratchcards)
print("Total number of scratchcards:", S)
