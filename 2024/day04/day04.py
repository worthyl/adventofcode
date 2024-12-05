
def count_word_occurrences(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    occurrences = 0

    # Function to check in bounds and match
    def check_match(r, c, dr, dc):
        for i in range(word_len):
            nr, nc = r + dr * i, c + dc * i
            if not (0 <= nr < rows and 0 <= nc < cols):
                return False
            if grid[nr][nc] != word[i]:
                return False
        return True

    # Directions: right, down, diagonal down-right, diagonal up-right
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_match(r, c, dr, dc):
                    occurrences += 1
                # Reverse direction to check for reversed words
                if check_match(r, c, -dr, -dc):
                    occurrences += 1

    return occurrences

def example():
    # Example usage with the provided word search
    grid = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]

    # Convert grid to list of lists
    grid = [list(row) for row in grid]

    # Count occurrences of XMAS
    return grid

def count_xmas_occurrences(grid):
    rows, cols = len(grid), len(grid)
    xmas_count = 0

    # Function to check if a diagonal is MAS or SAM
    def is_mas_pattern(chars):
        return chars in ['MAS', 'SAM']

    # Function to check an "X-MAS" pattern
    def check_xmas_pattern(r, c):
        # Ensure pattern is within grid bounds
        if not (0 <= r - 1 < rows and 0 <= r + 1 < rows and
                0 <= c - 1 < cols and 0 <= c + 1 < cols):
            return False

        # Get the diagonals
        diagonal1 = grid[r-1][c-1] + grid[r][c] + grid[r+1][c+1]
        diagonal2 = grid[r-1][c+1] + grid[r][c] + grid[r+1][c-1]

        # Check if both diagonals form MAS (in either direction)
        return (is_mas_pattern(diagonal1) and is_mas_pattern(diagonal2))

    # Iterate over each position in the grid
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            if check_xmas_pattern(r, c):
                xmas_count += 1

    return xmas_count

def get_input():
    with open("input.txt") as f:
        grid = f.read().strip().split("\n")
    return grid

def main():
    # grid = example()
    grid = get_input()
    result = count_word_occurrences(grid, "XMAS")
    print(result)
    result = count_xmas_occurrences(grid)
    print(result)
    # Output: 18

if __name__ == "__main__":
    main()
