import re


def sum_of_mul_instructions(memory):
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    matches = pattern.findall(memory)
    total_sum = sum(int(x) * int(y) for x, y in matches)
    return total_sum


def handle_instructions(memory):
    enable_multiplication = True
    total_sum = 0

    operations = re.split(r'(do\(\)|don\'t\(\)|mul\(\d+,\d+\))', memory)

    for op in operations:
        op = op.strip()
        if not op:
            continue

        if op == 'do()':
            enable_multiplication = True
        elif op == "don't()":
            enable_multiplication = False
        elif op.startswith('mul') and enable_multiplication:
            match = re.match(r'mul\((\d+),(\d+)\)', op)
            if match:
                x, y = map(int, match.groups())
                total_sum += x * y

    return total_sum


def main():
    with open("input.txt") as f:
        memory = f.read()
    part1 = sum_of_mul_instructions(memory)
    part2 = handle_instructions(memory)
    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
