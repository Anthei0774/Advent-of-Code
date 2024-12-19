program = """Register A: 0
Register B: 0
Register C: 9

Program: 2,6"""

program = """Register A: 10
Register B: 0
Register C: 0

Program: 5,0,5,1,5,4"""

# SZAR
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

# n = 0
# for suffix_length in range(1, len(program) + 1):

#     for offset in range(1, suffix_length + 1):
#         last_bits = program[-suffix_length:][-offset:]
#         print("Last bits:", last_bits)

#         pow = suffix_length - offset + 1

#         searching = {
#             n + s for s in range(8 ** (pow - 1), 8**pow, 8 ** (pow - 1))}
#         searching = {s: run_program([s, B, C]) for s in searching}
#         searching = {s: searching[s] for s in sorted(searching)}
#         print(searching)

#         output_last_bits = list(searching.values())
#         output_last_bits = [b[-offset:] for b in output_last_bits]

#         assert output_last_bits.count(last_bits) >= 1
#         idx = output_last_bits.index(last_bits)

#         if pow == suffix_length:
#             n = list(searching)[idx] - n
#         else:
#             n = list(searching)[idx]
#         print("n:", n)

# print(run_program([n, 0, 0]))

for n in range(300):
    print("n:", n, "; base-8 n:", list(format(n, 'o')),
          "; program:", run_program([n, 0, 0]))
