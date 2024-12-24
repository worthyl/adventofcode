from heapq import heappush, heappop
from dataclasses import dataclass
from functools import total_ordering
from typing import List, Tuple


@total_ordering
class State:
    x: int
    y: int
    direction: int  # 0:East, 1:South, 2:West, 3:North

    def __lt__(self, other):
        if not isinstance(other, State):
            return NotImplemented
        return (self.x, self.y, self.direction) < (other.x, other.y, other.direction)


def read_maze(filename: str) -> List[List[str]]:
    with open(filename, "r") as f:
        return [list(line.strip()) for line in f.readlines()]


def find_start_end(maze: List[List[str]]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    start = end = None
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == "S":
                start = (x, y)
            elif maze[y][x] == "E":
                end = (x, y)
    return start, end


def get_neighbors(state: State, maze: List[List[str]]) -> List[Tuple[State, int]]:
    neighbors = []
    # Movement vectors for East, South, West, North
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # Add rotations (clockwise and counterclockwise)
    neighbors.append(
        (State(state.x, state.y, (state.direction + 1) % 4), 1000)
    )  # Clockwise
    neighbors.append(
        (State(state.x, state.y, (state.direction - 1) % 4), 1000)
    )  # Counter-clockwise

    # Add forward movement
    dx, dy = directions[state.direction]
    new_x, new_y = state.x + dx, state.y + dy

    if (
        0 <= new_x < len(maze[0])
        and 0 <= new_y < len(maze)
        and maze[new_y][new_x] != "#"
    ):
        neighbors.append((State(new_x, new_y, state.direction), 1))

    return neighbors


def manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def solve_maze(maze: List[List[str]]) -> int:
    start_pos, end_pos = find_start_end(maze)
    initial_state = State(start_pos[0], start_pos[1], 0)  # Start facing East

    # Priority queue for A* algorithm
    # Add a unique counter to break ties between states with the same priority
    from itertools import count

    counter = count()
    queue = [
        (0, next(counter), initial_state)
    ]  # (estimated_total_cost, counter, state)
    visited = set()
    costs = {initial_state: 0}

    while queue:
        _, _, current_state = heappop(queue)
        current_cost = costs[current_state]

        if (current_state.x, current_state.y) == end_pos:
            return current_cost

        if current_state in visited:
            continue

        visited.add(current_state)

        for next_state, move_cost in get_neighbors(current_state, maze):
            new_cost = current_cost + move_cost

            if next_state not in costs or new_cost < costs[next_state]:
                costs[next_state] = new_cost
                priority = new_cost + manhattan_distance(
                    next_state.x, next_state.y, end_pos[0], end_pos[1]
                )
                heappush(queue, (priority, next(counter), next_state))

    return float("inf")


def main():
    maze = read_maze("input.txt")
    result = solve_maze(maze)
    print(f"Lowest possible score: {result}")


if __name__ == "__main__":
    main()
