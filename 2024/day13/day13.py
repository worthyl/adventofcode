from functools import lru_cache


def parse_input(filename):
    machines = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 4):
            if i + 2 >= len(lines):
                break

            button_a = lines[i].strip().split(': ')[1].split(', ')
            button_b = lines[i + 1].strip().split(': ')[1].split(', ')
            prize = lines[i + 2].strip().split(': ')[1].split(', ')

            a_x, a_y = int(button_a[0].split('+')[1]), int(button_a[1].split('+')[1])
            b_x, b_y = int(button_b[0].split('+')[1]), int(button_b[1].split('+')[1])
            prize_x, prize_y = int(prize[0].split('=')[1]), int(prize[1].split('=')[1])

            machines.append((a_x, a_y, b_x, b_y, prize_x, prize_y))
    return machines


@lru_cache(maxsize=None)
def min_tokens(target_x, target_y, a_x, a_y, b_x, b_y):
    if target_x == 0 and target_y == 0:
        return 0
    if target_x < 0 or target_y < 0:
        return float('inf')

    a_press = min_tokens(target_x - a_x, target_y - a_y, a_x, a_y, b_x, b_y) + 3
    b_press = min_tokens(target_x - b_x, target_y - b_y, a_x, a_y, b_x, b_y) + 1

    return min(a_press, b_press)


def calculate_min_tokens(machines):
    results = []
    for a_x, a_y, b_x, b_y, prize_x, prize_y in machines:
        tokens = min_tokens(prize_x, prize_y, a_x, a_y, b_x, b_y)
        results.append(tokens if tokens != float('inf') else None)
    return results


def main():
    machines = parse_input('input.txt')

    # Part 1
    print("Part 1:")
    min_tokens_list = calculate_min_tokens(machines)
    total_tokens = sum(tokens for tokens in min_tokens_list if tokens is not None)
    winnable_prizes = sum(1 for tokens in min_tokens_list if tokens is not None)
    print(f"Number of winnable prizes: {winnable_prizes}")
    print(f"Total tokens needed: {total_tokens}")

    # Part 2
    print("\nPart 2:")
    adjustment = 10000000000000
    adjusted_machines = [(a_x, a_y, b_x, b_y, prize_x + adjustment, prize_y + adjustment)
                         for a_x, a_y, b_x, b_y, prize_x, prize_y in machines]

    min_tokens.cache_clear()  # Clear the cache before Part 2
    min_tokens_list = calculate_min_tokens(adjusted_machines)
    total_tokens = sum(tokens for tokens in min_tokens_list if tokens is not None)
    winnable_prizes = sum(1 for tokens in min_tokens_list if tokens is not None)
    print(f"Number of winnable prizes: {winnable_prizes}")
    print(f"Total tokens needed: {total_tokens}")


if __name__ == "__main__":
    main()
