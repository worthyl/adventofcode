import sys
from collections import deque


def read_grid(filename='input.txt'):
    with open(filename) as f:
        return [[int(x) for x in row] for row in f.read().strip().split('\n')]


def is_valid(r, c, R, C):
    return 0 <= r < R and 0 <= c < C


def count_paths_bfs(grid, start_r, start_c):
    R, C = len(grid), len(grid[0])
    queue = deque([(start_r, start_c)])
    seen = set()
    count = 0

    while queue:
        r, c = queue.popleft()
        if (r, c) in seen:
            continue

        seen.add((r, c))
        if grid[r][c] == 0:
            count += 1

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc, R, C) and grid[nr][nc] == grid[r][c] - 1:
                queue.append((nr, nc))

    return count


def count_paths_dp(grid, r, c, memo=None):
    if memo is None:
        memo = {}

    if grid[r][c] == 0:
        return 1
    if (r, c) in memo:
        return memo[(r, c)]

    R, C = len(grid), len(grid[0])
    count = 0

    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = r + dr, c + dc
        if is_valid(nr, nc, R, C) and grid[nr][nc] == grid[r][c] - 1:
            count += count_paths_dp(grid, nr, nc, memo)

    memo[(r, c)] = count
    return count


def solve(grid):
    R, C = len(grid), len(grid[0])
    bfs_total = dp_total = 0

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 9:
                bfs_total += count_paths_bfs(grid, r, c)
                dp_total += count_paths_dp(grid, r, c)

    return bfs_total, dp_total


if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
    grid = read_grid(filename)
    p1, p2 = solve(grid)
    print(p1)
    print(p2)
