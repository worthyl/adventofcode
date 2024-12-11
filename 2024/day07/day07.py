from itertools import product

def read_equations_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def parse_equations(lines):
    equations = []
    for line in lines:
        target, numbers = line.split(":")
        target = int(target.strip())
        numbers = list(map(int, numbers.strip().split()))
        equations.append((target, numbers))
    return equations


def evaluate_left_to_right(expression):
    tokens = expression.replace('+', ' + ').replace('*', ' * ').replace('||', ' || ').split()
    result = int(tokens[0])

    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        operand = int(tokens[i + 1])

        if operator == '+':
            result += operand
        if operator == '*':
            result *= operand
        elif operator == '||':
            result = int(str(result) + str(operand))

    return result

def evaluate_equation(target, numbers, cycle):
    operators = ['+', '*']
    if cycle == 'p2':
        operators = ['+', '*', '||']
    n = len(numbers)

    for ops in product(operators, repeat=n-1):
        expression = str(numbers[0])
        for i in range(1, n):
            expression += ops[i-1] + str(numbers[i])
        if evaluate_left_to_right(expression) == target:
            # print(target, expression)
            return True
    return False

def total_calibration_result(equations, cycle):
    total = 0
    for equation in equations:
        target, numbers = equation
        if evaluate_equation(target, numbers, cycle):
            total += target
    return total

def main():
    # Replace 'input.txt' with your actual input file path
    file_path = 'input.txt'
    lines = read_equations_file(file_path)
    equations = parse_equations(lines)
    result = total_calibration_result(equations, 'p1')
    print(f"Total calibration result for part1: {result}")

    equations = parse_equations(lines)
    result = total_calibration_result(equations, 'p2')
    print(f"Total calibration result for part2: {result}")

if __name__ == "__main__":
    main()
