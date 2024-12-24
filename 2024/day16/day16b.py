from dataclasses import dataclass
import sys
import z3
import re
import heapq
from collections import defaultdict, Counter, deque
from sympy.solvers.solveset import linsolve
import pyperclip as pc


@dataclass(frozen=True)
class Position:
    row: int
    col: int


@dataclass(frozen=True)
class State:
    pos: Position
    direction: int


@dataclass
class Grid:
    cells: list[list[str]]
    rows: int
    cols: int
    start: Position
    end: Position

    @classmethod
    def from_file(cls, filename):
        data = open(filename).read().strip()
        grid = data.split("\n")
        rows = len(grid)
        cols = len(grid[0])
        cells = [[grid[r][c] for c in range(cols)] for r in range(rows)]

        start = end = None
        for r in range(rows):
            for c in range(cols):
                if cells[r][c] == "S":
                    start = Position(r, c)
                elif cells[r][c] == "E":
                    end = Position(r, c)

        return cls(cells, rows, cols, start, end)

    def is_valid_position(self, pos: Position) -> bool:
        return (
            0 <= pos.col < self.cols
            and 0 <= pos.row < self.rows
            and self.cells[pos.row][pos.col] != "#"
        )


def pr(s):
    print(s)
    pc.copy(s)


DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up right down left


def find_paths(
    grid: Grid, start: Position, end: Position, reverse: bool = False
) -> dict:
    q = []
    seen = set()
    dist = {}
    best = None

    for dir in range(4) if reverse else [1]:
        initial_state = State(start if not reverse else end, dir)
        heapq.heappush(q, (0, initial_state))

    while q:
        d, state = heapq.heappop(q)
        if state not in dist:
            dist[state] = d

        if not reverse and state.pos == end and best is None:
            best = d

        if state in seen:
            continue

        seen.add(state)
        dr, dc = DIRS[state.direction]
        new_pos = Position(
            state.pos.row + (-dr if reverse else dr),
            state.pos.col + (-dc if reverse else dc),
        )

        if grid.is_valid_position(new_pos):
            heapq.heappush(q, (d + 1, State(new_pos, state.direction)))

        for turn in [(state.direction + 1) % 4, (state.direction + 3) % 4]:
            heapq.heappush(q, (d + 1000, State(state.pos, turn)))

    return dist, best


def main():
    infile = sys.argv[1] if len(sys.argv) >= 2 else "input.txt"
    grid = Grid.from_file(infile)

    forward_dist, best = find_paths(grid, grid.start, grid.end)
    backward_dist, _ = find_paths(grid, grid.start, grid.end, reverse=True)

    ok = set()
    for r in range(grid.rows):
        for c in range(grid.cols):
            pos = Position(r, c)
            for dir in range(4):
                state = State(pos, dir)
                if (
                    state in forward_dist
                    and state in backward_dist
                    and forward_dist[state] + backward_dist[state] == best
                ):
                    ok.add(pos)

    print(best)
    print(len(ok))


if __name__ == "__main__":
    main()
