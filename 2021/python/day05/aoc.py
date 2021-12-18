from collections import defaultdict


def part_one(lines: int) -> int:
    pairs_to_lines = defaultdict(int)
    for start, end in lines:
        if start[0] == end[0] or start[1] == end[1]:
            add_lines(pairs_to_lines, start, end)

    print(f'Part 1: {count_points_overlap(pairs_to_lines)}')
    return


def part_two(lines: int) -> int:
    pairs_to_lines = defaultdict(int)
    for start, end in lines:
        add_lines(pairs_to_lines, start, end)

    print(f'Part 2: {count_points_overlap(pairs_to_lines)}')
    return


def read_input(filename: str) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    with open(filename) as f:
        lines = list(map(lambda line: line.strip().split(" -> "), f.readlines()))

    lines = [
        tuple(
            [tuple(map(int, line[0].split(","))), tuple(map(int, line[1].split(",")))]
        )
        for line in lines
    ]
    return lines


def count_points_overlap(pairs_to_lines: dict[tuple[int, int], int]) -> int:
    counter = 0
    for lines in pairs_to_lines.values():
        if lines >= 2:
            counter += 1

    return counter


def add_lines(
    pairs_to_lines: dict[tuple[int, int], int],
    start: tuple[int, int],
    end: tuple[int, int],
) -> None:
    x_step = (
        0 if end[0] == start[0] else int(end[0] - start[0]) / abs(end[0] - start[0])
    )
    y_step = (
        0 if end[1] == start[1] else int(end[1] - start[1]) / abs(end[1] - start[1])
    )

    dist = max(abs(end[0] - start[0]), abs(end[1] - start[1]))

    for i in range(dist + 1):
        x = start[0] + i * x_step
        y = start[1] + i * y_step
        pairs_to_lines[(x, y)] += 1
    return pairs_to_lines


def print_lines(pairs_to_lines: dict[tuple[int, int], int]) -> None:
    """
    :type pairs_to_lines: object
    """
    x_min = min([coord[0] for coord in pairs_to_lines])
    x_max = max([coord[0] for coord in pairs_to_lines])
    y_min = min([coord[1] for coord in pairs_to_lines])
    y_max = max([coord[1] for coord in pairs_to_lines])

    for y in range(y_min, y_max + 1):
        line = ''
        for x in range(x_min, x_max + 1):
            if pairs_to_lines[(x, y)] <= 0:
                line = line.append('.')
            else:
                line = line.append(str(pairs_to_lines[(x, y)]))
        print(line)


if __name__ == "__main__":
    file = "input.txt"
    lines = read_input(file)
    part_one(lines)
    part_two(lines)