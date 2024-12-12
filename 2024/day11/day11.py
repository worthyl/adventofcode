def optimized_evolve_stones(stones, blinks):
    DP = {}
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            # Rule 1: If stone is 0, replace with 1
            if (stones, blinks) in DP:

            elif stone == 0:
                new_stones.append(1)
            else:
                # Convert stone to string once
                stone_str = str(stone)
                length = len(stone_str)
                # Rule 2: If stone has even number of digits, split it
                if length % 2 == 0:
                    half_len = length // 2
                    left = int(stone_str[:half_len])
                    right = int(stone_str[half_len:])
                    new_stones.extend([left, right])
                # Rule 3: Multiply by 2024
                else:
                    new_stones.append(stone * 2024)
        stones = new_stones
    return stones



# Test the program
def main():
    # Initial stones
    # initial_stones = [125, 17]
    initial_stones = [8793800, 1629, 65, 5, 960, 0, 138983, 85629]
    # Number of blinks
    blinks = 25

    # Evolve stones and print results
    final_stones = optimized_evolve_stones(initial_stones, blinks)
    print(f"Number of stones after {blinks} blinks: {len(final_stones)}")

    # Print first few transformations for verification
    for test_blinks in range(1, 26):
        stones = optimized_evolve_stones(initial_stones, test_blinks)
        print(f"After {test_blinks} blinks: {len(stones)}")

    for test_blinks in range(1, 76):
        stones = optimized_evolve_stones(initial_stones, test_blinks)
        print(f"After {test_blinks} blinks: {len(stones)}")


if __name__ == "__main__":
    main()
