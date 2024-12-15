def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    robots = []
    for line in lines:
        position, velocity = line.strip().split(' ')
        p_x, p_y = map(int, position[2:].split(','))
        v_x, v_y = map(int, velocity[2:].split(','))
        robots.append(((p_x, p_y), (v_x, v_y)))
    return robots

def simulate_robots(robots, width, height, seconds):
    for _ in range(seconds):
        new_positions = []
        for (p_x, p_y), (v_x, v_y) in robots:
            new_x = (p_x + v_x) % width
            new_y = (p_y + v_y) % height
            new_positions.append((new_x, new_y))
        robots = [(pos, vel) for pos, vel in zip(new_positions, [vel for _, vel in robots])]
    return [pos for pos, _ in robots]

def count_robots_in_quadrants(positions, width, height):
    mid_x = width // 2
    mid_y = height // 2
    quadrants = [0, 0, 0, 0]  # top-left, top-right, bottom-left, bottom-right
    for x, y in positions:
        if x == mid_x or y == mid_y:
            continue
        if x < mid_x and y < mid_y:
            quadrants[0] += 1
        elif x >= mid_x and y < mid_y:
            quadrants[1] += 1
        elif x < mid_x and y >= mid_y:
            quadrants[2] += 1
        elif x >= mid_x and y >= mid_y:
            quadrants[3] += 1
    return quadrants

def calculate_safety_factor(quadrants):
    factor = 1
    for count in quadrants:
        factor *= count
    return factor

def main():
    width, height = 101, 103
    robots = parse_input("input.txt")
    positions_after_100_seconds = simulate_robots(robots, width, height, 100)
    quadrants = count_robots_in_quadrants(positions_after_100_seconds, width, height)
    safety_factor = calculate_safety_factor(quadrants)
    print(safety_factor)

if __name__ == '__main__':
    main()