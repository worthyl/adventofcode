def count_unique_antinodes(antenna_map):
    rows = len(antenna_map)
    cols = len(antenna_map[0])
    antennas = {}

    collect_antenna_positions_by_freq(antenna_map, antennas, cols, rows)

    antinodes = set()

    # calculate_antinodes_by_frequency(antennas, antinodes, cols, rows, "p1")

    # Calculate antinodes for each frequency
    for freq, positions in antennas.items():
        n = len(positions)
        for i in range(n):
            for j in range(i+1, n):
                r1, c1 = positions[i]
                r2, c2 = positions[j]

                # Calculate the vector between the two antennas
                dr = r2 - r1
                dc = c2 - c1

                # Calculate potential antinode positions
                r3, c3 = r1 - dr, c1 - dc
                r4, c4 = r2 + dr, c2 + dc

                # Add antinodes if they're within the map bounds
                if 0 <= r3 < rows and 0 <= c3 < cols:
                    antinodes.add((r3, c3))
                if 0 <= r4 < rows and 0 <= c4 < cols:
                    antinodes.add((r4, c4))

    return len(antinodes)


def collect_antenna_positions_by_freq(antenna_map, antennas, cols, rows):
    # Collect all antenna positions by frequency
    for r in range(rows):
        for c in range(cols):
            freq = antenna_map[r][c]
            if freq != '.':
                if freq not in antennas:
                    antennas[freq] = []
                antennas[freq].append((r, c))


def count_unique_antinodes_with_harmonics(antenna_map):
    rows = len(antenna_map)
    cols = len(antenna_map[0])
    antennas = {}

    collect_antenna_positions_by_freq(antenna_map, antennas, cols, rows)

    antinodes = set()

    calculate_antinodes_by_frequency(antennas, antinodes, cols, rows, "p2")

    return len(antinodes)


def calculate_antinodes_by_frequency(antennas, antinodes, cols, rows, problem):
    # Calculate antinodes for each frequency
    for freq, positions in antennas.items():
        n = len(positions)
        if problem == "p2":
            if n < 2:
                continue  # No antinodes possible with fewer than 2 antennas

            # Add each antenna's position as an antinode
            for pos in positions:
                antinodes.add(pos)

        # Check for all pairs of antennas to find aligned points
        for i in range(n):
            for j in range(i + 1, n):
                r1, c1 = positions[i]
                r2, c2 = positions[j]

                # Determine the direction vector between the two antennas
                dr = r2 - r1
                dc = c2 - c1

                # Normalize the direction vector to its smallest integer step
                gcd = abs(__import__('math').gcd(dr, dc))
                dr //= gcd
                dc //= gcd

                # Generate all intermediate points between the two antennas and beyond
                k = 1
                while True:
                    r3, c3 = r1 - k * dr, c1 - k * dc  # Extend backward
                    r4, c4 = r2 + k * dr, c2 + k * dc  # Extend forward

                    added_any = False

                    if 0 <= r3 < rows and 0 <= c3 < cols:
                        antinodes.add((r3, c3))
                        added_any = True

                    if 0 <= r4 < rows and 0 <= c4 < cols:
                        antinodes.add((r4, c4))
                        added_any = True

                    if problem == "p2":

                        if not added_any:
                            break

                        k += 1


# Example input
antenna_map = [
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............"
]

def main():

    """Reads the input file and returns the map as a list of strings."""
    with open("input.txt", 'r') as file:
        antenna_map = [line.strip() for line in file.readlines()]

    result = count_unique_antinodes(antenna_map)
    print(f"Number of unique antinodes: {result}")

    result = count_unique_antinodes_with_harmonics(antenna_map)
    print(f"Number of unique antinodes: {result}")


if __name__ == "__main__":
    main()