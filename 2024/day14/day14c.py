import sys
from collections import deque

# Constants
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left


def parse_ints(s):
    """Extract integers from a string."""
    return [int(x) for x in s.replace(',', ' ').split()]


def simulate_robots(robots, width, height, max_time):
    """Simulate robot movement and check for patterns."""
    for t in range(1, max_time + 1):
        grid = [['.'] * width for _ in range(height)]

        # Update robot positions
        for i, (px, py, vx, vy) in enumerate(robots):
            px = (px + vx) % width
            py = (py + vy) % height
            robots[i] = (px, py, vx, vy)
            grid[py][px] = '#'

        # Part 1: Calculate quadrant counts at t=100
        if t == 100:
            mx, my = width // 2, height // 2
            q = [0] * 4
            for px, py, _, _ in robots:
                if px != mx and py != my:
                    q_index = (px > mx) + 2 * (py > my)
                    q[q_index] += 1
            print("Part 1:", q[0] * q[1] * q[2] * q[3])

        # Part 2: Check for Christmas tree pattern
        components = count_components(grid, width, height)
        if components <= 200:
            print("Part 2:", t)
            print_grid(grid)
            break


def count_components(grid, width, height):
    """Count connected components in the grid."""
    seen = set()
    components = 0
    for x in range(width):
        for y in range(height):
            if grid[y][x] == '#' and (x, y) not in seen:
                components += 1
                bfs(grid, x, y, seen, width, height)
    return components


def bfs(grid, start_x, start_y, seen, width, height):
    """Perform BFS to mark connected components."""
    queue = deque([(start_x, start_y)])
    while queue:
        x, y = queue.popleft()
        if (x, y) in seen:
            continue
        seen.add((x, y))
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == '#':
                queue.append((nx, ny))


def print_grid(grid):
    """Print the grid."""
    for row in grid:
        print(''.join(row))


def main():
    infile = "input.txt"
