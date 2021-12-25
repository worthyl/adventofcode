def run(filename: str):

    total_area = 0
    total_ribbon = 0

    with open(filename) as file:
        lines = [line.rstrip() for line in file]

    for line in lines:
        dimensions = line.split("x")
        map_ints = list(map(int, dimensions))
        map_ints.sort()
        A0 = map_ints[0] * map_ints[1]
        A1 = map_ints[0] * map_ints[2]
        A2 = map_ints[1] * map_ints[2]
        slack = min(A0, A1, A2)
        area = 2*A0 + 2*A1 + 2*A2 + slack
        total_area += area
        ribbon = (2*(map_ints[0]+map_ints[1])) + (map_ints[0]*map_ints[1]*map_ints[2])
        total_ribbon += ribbon

    print(f'Total Area: {total_area}')
    print(f'Total Ribbon: {total_ribbon}')

if __name__ == '__main__':
    run('input.txt')
