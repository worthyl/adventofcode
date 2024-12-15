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

def is_christmas_tree_pattern(positions, width, height):
    # Create a grid to visualize robot positions
    grid = [[0 for _ in range(width)] for _ in range(height)]
    for x, y in positions:
        grid[y][x] += 1

    # Check for tree shape characteristics
    # 1. Should have a triangular shape
    # 2. Should have a trunk at the bottom
    # 3. Most robots should participate in the pattern

    mid_x = width // 2
    tree_width = 1
    tree_found = True
    trunk_height = 3
    tree_height = height // 3

    # Check trunk
    for y in range(height - trunk_height, height):
        if sum(grid[y][mid_x - 1:mid_x + 2]) < 1:
            tree_found = False
            break

    # Check triangle
    start_y = height - trunk_height - tree_height
    for y in range(start_y, height - trunk_height):
        expected_width = (height - trunk_height - y) // 2
        if sum(grid[y][mid_x - expected_width:mid_x + expected_width + 1]) < expected_width:
            tree_found = False
            break

    # Check if most robots participate
    total_robots = sum(sum(row) for row in grid)
    tree_robots = sum(sum(row[mid_x - tree_width:mid_x + tree_width + 1])
                      for row in grid[start_y:height])

    return tree_found and (tree_robots > total_robots * 0.8)


def find_christmas_tree_time(file_path):
    width, height = 101, 103
    robots = parse_input(file_path)
    seconds = 0
    max_time = 10000  # Prevent infinite loop

    while seconds < max_time:
        positions = simulate_robots(robots, width, height, 1)
        seconds += 1
        if is_christmas_tree_pattern(positions, width, height):
            return seconds
    return None


def main():
    # Part 1
    width, height = 101, 103
    robots = parse_input("input.txt")
    positions_after_100_seconds = simulate_robots(robots, width, height, 100)
    quadrants = count_robots_in_quadrants(positions_after_100_seconds, width, height)
    safety_factor = calculate_safety_factor(quadrants)
    print(safety_factor)
    print(find_christmas_tree_time("input.txt"))

    # Part 2
    tree_time = find_christmas_tree_time("input.txt")

    return safety_factor, tree_time


if __name__ == '__main__':
    main()
