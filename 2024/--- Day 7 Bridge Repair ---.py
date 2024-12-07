equations = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

with open("2024/inputs/7.txt") as f:
    equations = f.read()

equations = equations.split("\n")
equations = [eq.replace(":", "").split(" ") for eq in equations]
equations = [list(map(int, eq)) for eq in equations]

################################################################################
# PART 1

# orignally I tried to solve this by generating all combinations of + and * signs. While it produced the good solution (earned the star), it was ridiculously slow, took more than 5 mins to complete. I realized, since we execute the operands from left-to-right, it does make sense to check if the result is divisible by the last value. If it does not, then we can omit the multiplication branch, thus potentially reduce the calculations. Tried it, and the code finished in just a matter of seconds.


def solve_equation(eq):

    # early abort
    if eq[0] < 0:
        return False

    # final pass
    if len(eq) == 2:
        return eq[0] == eq[1]

    # divisibility check as indicated in the comment
    if eq[0] % eq[-1] == 0:
        sub_eq = eq[:-1]
        sub_eq[0] = eq[0] // eq[-1]

        # "return" statement only if the sub_eq is solvable. If we would simply return the sub_eq result, then the addition part does not run
        if solve_equation(sub_eq):
            return True

    # check addition
    sub_eq = eq[:-1]
    sub_eq[0] = eq[0] - eq[-1]
    return solve_equation(sub_eq)


s = 0
for eq in equations:
    if solve_equation(eq):
        s += eq[0]

print("Total calibration result:", s)

################################################################################
# PART 2


def solve_equation(eq):

    # early abort
    if eq[0] < 0:
        return False

    # final pass
    if len(eq) == 2:
        return eq[0] == eq[1]

    # divisibility check as indicated in the comment
    if eq[0] % eq[-1] == 0:
        sub_eq = eq[:-1]
        sub_eq[0] = eq[0] // eq[-1]

        # "return" statement only if the sub_eq is solvable. If we would simply return the sub_eq result, then the addition part does not run
        if solve_equation(sub_eq):
            return True

    # removability check. Exact same as the multiplication block otherwise
    end = str(eq[-1])
    l = len(end)
    if end == str(eq[0])[-l:]:
        sub_eq = eq[:-1]

        # it is expected that during this procedure the left-hand-side results in an empty string. In this case, concatenation is not an option
        try:
            sub_eq[0] = int(str(sub_eq[0])[:-l])
            if solve_equation(sub_eq):
                return True
        except ValueError:
            pass

    # check addition
    sub_eq = eq[:-1]
    sub_eq[0] = eq[0] - eq[-1]
    return solve_equation(sub_eq)


s = 0
for eq in equations:
    if solve_equation(eq):
        s += eq[0]

print("Total calibration result:", s)
