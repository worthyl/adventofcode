
from statistics import median


def part_one(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(int, f.read().strip().split(",")))

    p1 = int(sum([abs(median(nums) - num) for num in nums]))
    print(f'Part 1: {p1}')


def part_two(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(int, f.read().strip().split(",")))

    p2 = min(
        [
            sum([fuel(x, point) for x in nums])
            for point in range(min(nums), max(nums) + 1)
        ]
    )
    print(f'Part 2: {p2}')


def fuel(start, end: int) -> int:
    d = max(start, end) - min(start, end)
    return int(d * (d + 1) / 2)


if __name__ == "__main__":
    input_path = "input.txt"
    part_one(input_path)
    part_two(input_path)