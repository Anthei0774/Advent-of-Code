program = """Register A: 0
Register B: 0
Register C: 9

Program: 2,6"""

program = """Register A: 10
Register B: 0
Register C: 0

Program: 5,0,5,1,5,4"""

program = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

program = """Register A: 0
Register B: 29
Register C: 0

Program: 1,7"""

program = """Register A: 0
Register B: 2024
Register C: 43690

Program: 4,0"""

program = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

with open("2024/inputs/17.txt") as f:
    program = f.read()

program = program.split("\n")

A = int(program[0].split(" ")[-1])
B = int(program[1].split(" ")[-1])
C = int(program[2].split(" ")[-1])

program = program[-1].split(" ")[-1].split(",")
program = list(map(int, program))

################################################################################
# PART 1
################################################################################


def run_program(registers):

    [A, B, C] = registers

    outputs = []
    i = 0
    while i < len(program):
        # print("i:", i)
        # print("Registers: A =", A, ", B =", B, ", C =", C)

        values = [0, 1, 2, 3, A, B, C]

        opcode = program[i]
        operand = program[i + 1]

        # adv = A-Division
        if opcode == 0:
            A = A // (2 ** values[operand])

        # bxl = B-XOR-Literal
        elif opcode == 1:
            B = B ^ operand

        # bst = B-???
        elif opcode == 2:
            B = values[operand] % 8

        # jnz = Jump-Non-Zero
        elif opcode == 3:
            if A != 0:
                i = operand
                continue

        # bxc = B-Xor-C
        elif opcode == 4:
            B = B ^ C
        # out
        elif opcode == 5:
            outputs.append(values[operand] % 8)

        # bdv = B-Division
        elif opcode == 6:
            B = A // (2 ** values[operand])

        # cdv = C-Division
        else:
            assert opcode == 7, "ERROR"
            C = A // (2 ** values[operand])

        i += 2

    return outputs


outputs = run_program([A, B, C])
outputs = list(map(str, outputs))
outputs = ",".join(outputs)
print("Outputs:", outputs)

################################################################################
# PART 2
################################################################################

# breadth-first search for the digits of A in base 8
candidates = [[[0 for _ in range(len(program))]]]

# i marks the position of the digit in A
for i in range(len(program)):

    # next stores the candidates solutions for the digit i
    next = []
    for c in candidates[-1]:

        # try out all possible digits (0-7) for the i-th digit of A
        for j in range(8):
            tmp = c.copy()
            tmp[i] = j

            n = list(map(str, tmp))
            n = "".join(n)
            n = int(n, 8)

            # test and if good, append to next
            result = run_program([n, B, C])
            end = -(i + 1)
            if program[end:] == result[end:]:
                next.append(tmp)

    candidates.append(next)

# min search
N = float("inf")
for c in candidates[-1]:
    n = list(map(str, c))
    n = "".join(n)
    n = int(n, 8)
    result = run_program([n, B, C])

    # all solutions in the end of candidates should produce the program
    assert program == result

    if n < N:
        N = n

print("N:", N)
