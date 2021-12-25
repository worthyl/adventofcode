def run(filename: str):
    floor = 0

    with open(filename) as f:
        lines = f.readlines()

    for instruction in lines:
        for i, c in enumerate(instruction):
            if c == '(':
                floor = floor + 1
            elif c == ')':
                floor = floor - 1
            if floor == -1:
                print(f'Basement reached: {i + 1}')

    print(f'Floor: {floor}')


if __name__ == '__main__':
    run('input.txt')
