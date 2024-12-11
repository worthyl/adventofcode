from typing import List, Set, Tuple
import numpy as np


def read_field() -> Tuple[np.ndarray, int, int, int, int]:
    with open("input.txt") as f:
        field = np.array([list(l.strip()) for l in f])

    NY, NX = field.shape
    start = np.where(np.isin(field, list("<>^v")))
    sy, sx = start[0][0], start[1][0]
    d = "^>v<".find(field[sy, sx])
    field[sy, sx] = "x"

    return field, sx, sy, d, NX, NY


def game(x: int, y: int, d: int, field: np.ndarray, NX: int, NY: int) -> int:
    # Pre-compute direction arrays for better performance
    dx = np.array([0, 1, 0, -1])
    dy = np.array([-1, 0, 1, 0])

    while True:
        nx, ny = x + dx[d], y + dy[d]
        if not (0 <= nx < NX and 0 <= ny < NY):
            return np.sum(field == "x")

        if field[ny, nx] == "#":
            d = (d + 1) % 4
        else:
            field[ny, nx] = "x"
            x, y = nx, ny


def game_with_loop(x: int, y: int, d: int, field: np.ndarray,
                   ox: int, oy: int, NX: int, NY: int) -> int:
    field = field.copy()
    field[oy, ox] = "#"
    visited: Set[Tuple[int, int, int]] = set()

    # Pre-compute direction arrays
    dx = np.array([0, 1, 0, -1])
    dy = np.array([-1, 0, 1, 0])

    while True:
        state = (x, y, d)
        if state in visited:
            return 1
        visited.add(state)

        nx, ny = x + dx[d], y + dy[d]
        if not (0 <= nx < NX and 0 <= ny < NY):
            return 0

        if field[ny, nx] == "#":
            d = (d + 1) % 4
        else:
            field[ny, nx] = "x"
            x, y = nx, ny


def main():
    field, sx, sy, d, NX, NY = read_field()
    print(game(sx, sy, d, field.copy(), NX, NY))

    dots = np.where(field == ".")
    result = sum(game_with_loop(sx, sy, d, field, x, y, NX, NY)
                 for y, x in zip(dots[0], dots[1]))
    print(result)


if __name__ == "__main__":
    main()
