machines = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

with open("2024/inputs/13.txt") as f:
    machines = f.read()

assert "-" not in machines
machines = machines.replace(":", "").replace(",", "")
machines = machines.split("\n")

i = 0
while i < len(machines):

    A = machines[i].split(" ")
    A = A[2:]
    A = [int(coord[2:]) for coord in A]

    B = machines[i + 1].split(" ")
    B = B[2:]
    B = [int(coord[2:]) for coord in B]

    prize = machines[i + 2].split(" ")
    prize = prize[1:]
    prize = [int(coord[2:]) for coord in prize]

    machines[i] = {"A": A, "B": B, "price": prize}
    i += 4

machines = [machines[i] for i in range(0, len(machines), 4)]

################################################################################
# PART 1-2


def calculate_tokens_needed(machines, offset=0):

    # for every machine, we need to solve xA * yB = price, so linear algebra go brrrrrrr :D

    S = 0
    for m in machines:

        m["price"][0] += offset
        m["price"][1] += offset

        det = m["A"][0] * m["B"][1] - m["A"][1] * m["B"][0]
        assert det != 0

        # use Cramer's rule to get x and y

        # for both, we are working with whole positive numbers, and any violation of this marks the equation unsolvable

        # side note, that the determinant above could be still 0 with the equation solvable, but I had luck with my input

        x = m["price"][0] * m["B"][1] - m["price"][1] * m["B"][0]
        if x % det != 0:
            continue
        x //= det
        if x < 0:
            continue

        y = m["A"][0] * m["price"][1] - m["A"][1] * m["price"][0]
        if y % det != 0:
            continue
        y //= det
        if y < 0:
            continue

        S += (3 * x + y)

    print("Tokens needed:", S)


calculate_tokens_needed(machines)
calculate_tokens_needed(machines, 10000000000000)
