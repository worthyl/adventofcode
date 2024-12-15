def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    map_lines = []
    moves = ""
    for line in lines:
        if line.strip() and not line.strip().startswith('<') and not line.strip().endswith('>'):
            map_lines.append(line.strip())
        else:
            moves += line.strip()
    return map_lines, moves

def find_robot_and_boxes(map_lines):
    robot_pos = None
    boxes = []
    for y, line in enumerate(map_lines):
        for x, char in enumerate(line):
            if char == '@':
                robot_pos = (x, y)
            elif char == 'O':
                boxes.append((x, y))
    return robot_pos, boxes

def move_robot(map_lines, robot_pos, boxes, moves):
    directions = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}
    for move in moves:
        dx, dy = directions[move]
        new_robot_pos = (robot_pos[0] + dx, robot_pos[1] + dy)
        if map_lines[new_robot_pos[1]][new_robot_pos[0]] == '#':
            continue  # Robot cannot move into a wall
        if new_robot_pos in boxes:
            new_box_pos = (new_robot_pos[0] + dx, new_robot_pos[1] + dy)
            if map_lines[new_box_pos[1]][new_box_pos[0]] == '#' or new_box_pos in boxes:
                continue  # Box cannot be pushed into a wall or another box
            boxes.remove(new_robot_pos)
            boxes.append(new_box_pos)
        robot_pos = new_robot_pos
    return robot_pos, boxes

def calculate_gps_sum(boxes):
    return sum(100 * box[1] + box[0] for box in boxes)

def main():
    map_lines, moves = read_input('input.txt')
    robot_pos, boxes = find_robot_and_boxes(map_lines)
    robot_pos, boxes = move_robot(map_lines, robot_pos, boxes, moves)
    gps_sum = calculate_gps_sum(boxes)
    print(f"Sum of all boxes' GPS coordinates: {gps_sum}")

    # Test with the provided example
    example_map = [
        "########",
        "#..O.O.#",
        "##@.O..#",
        "#...O..#",
        "#.#.O..#",
        "#...O..#",
        "#......#",
        "########"
    ]
    example_moves = "<^^>>>vv<v>>v<<"
    robot_pos, boxes = find_robot_and_boxes(example_map)
    robot_pos, boxes = move_robot(example_map, robot_pos, boxes, example_moves)
    example_gps_sum = calculate_gps_sum(boxes)
    print(f"Example sum of all boxes' GPS coordinates: {example_gps_sum}")

if __name__ == "__main__":
    main()
