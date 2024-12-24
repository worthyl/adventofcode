import heapq
from typing import List, Tuple, Set


class MazeSolver:
    def __init__(self, maze: List[List[int]]):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    def heuristic(self, current: Tuple[int, int], goal: Tuple[int, int]) -> int:
        # Manhattan distance heuristic
        return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

    def get_neighbors(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        neighbors = []
        for dx, dy in self.directions:
            new_x, new_y = pos[0] + dx, pos[1] + dy
            if (
                0 <= new_x < self.rows
                and 0 <= new_y < self.cols
                and self.maze[new_x][new_y] == 0
            ):
                neighbors.append((new_x, new_y))
        return neighbors

    def solve(
        self, start: Tuple[int, int], goal: Tuple[int, int]
    ) -> List[Tuple[int, int]]:
        # Priority queue for A* algorithm
        pq = [(0, start)]
        came_from = {start: None}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, goal)}
        visited = set()

        while pq:
            _, current = heapq.heappop(pq)

            if current == goal:
                path = []
                while current:
                    path.append(current)
                    current = came_from[current]
                return path[::-1]

            visited.add(current)

            for neighbor in self.get_neighbors(current):
                if neighbor in visited:
                    continue

                tentative_g = g_score[current] + 1

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self.heuristic(neighbor, goal)
                    heapq.heappush(pq, (f_score[neighbor], neighbor))

        return []  # No path found


def read_maze(filename: str) -> List[List[int]]:
    maze = []
    with open(filename, "r") as f:
        for line in f:
            # Convert each character to int, assuming 0 for path and 1 for wall
            row = [1 if c == "#" else '0' if c == '.' else int(c) for c in line.strip( ) ]
            maze.append(row)
    return maze


def print_maze(maze: List[List[int]], path: List[Tuple[int, int]] = None):
    if path:
        path_set = set(path)

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if path and (i, j) in path_set:
                print("*", end="")
            elif maze[i][j] == 1:
                print("█", end="")
            else:
                print(" ", end="")
        print()


def main():
    # Read maze from file
    maze = read_maze("input.txt")
    solver = MazeSolver(maze)

    # Find start and goal positions (assuming top-left to bottom-right)
    start = (0, 0)
    goal = (len(maze) - 1, len(maze[0]) - 1)

    # Solve the maze
    path = solver.solve(start, goal)

    if path:
        print("Solution found!")
        print_maze(maze, path)
    else:
        print("No solution exists!")


if __name__ == "__main__":
    main()
