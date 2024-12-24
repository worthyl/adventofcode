def read_input(filename):
    # Read initial register values and program
    with open(filename, "r") as file:
        lines = file.readlines()

    # Parse register values
    a = int(lines[0].split(": ")[1])
    b = int(lines[1].split(": ")[1])
    c = int(lines[2].split(": ")[1])

    # Parse program
    code = lines[4].strip().split(":")[1]
    program = [int(x) for x in code.split(",")]

    return a, b, c, program


def get_combo_value(operand, a, b, c):
    if operand <= 3:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    return 0  # operand 7 is reserved


def run_program(a, b, c, program):
    outputs = []
    ip = 0  # instruction pointer

    while ip < len(program) - 1:
        opcode = program[ip]
        operand = program[ip + 1]

        if opcode == 0:  # adv
            power = get_combo_value(operand, a, b, c)
            a = a // (2**power)
        elif opcode == 1:  # bxl
            b = b ^ operand
        elif opcode == 2:  # bst
            b = get_combo_value(operand, a, b, c) % 8
        elif opcode == 3:  # jnz
            if a != 0:
                ip = operand
                continue
        elif opcode == 4:  # bxc
            b = b ^ c
        elif opcode == 5:  # out
            value = get_combo_value(operand, a, b, c) % 8
            outputs.append(str(value))
        elif opcode == 6:  # bdv
            power = get_combo_value(operand, a, b, c)
            b = a // (2**power)
        elif opcode == 7:  # cdv
            power = get_combo_value(operand, a, b, c)
            c = a // (2**power)

        ip += 2

    return ",".join(outputs)


def main():
    # Read input and initialize registers
    a, b, c, program = read_input("input.txt")

    # Run program and get output
    result = run_program(a, b, c, program)
    print(result)
    i = 0
    for i in range(0,10000000):
        result = run_program(i, b, c, program)
        if result == program:
            print(i)
            break




if __name__ == "__main__":
    main()
