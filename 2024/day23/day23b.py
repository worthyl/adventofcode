from collections import defaultdict
from itertools import combinations


def read_connections(filename):
    # Create adjacency list representation
    graph = defaultdict(set)
    with open(filename, "r") as file:
        for line in file:
            a, b = line.strip().split("-")
            graph[a].add(b)
            graph[b].add(a)
    return graph


def find_largest_clique(graph):
    # Get all nodes
    nodes = list(graph.keys())
    max_clique = []
    max_size = 0

    # Check all possible combinations of nodes
    for size in range(3, len(nodes) + 1):
        for clique in combinations(nodes, size):
            # Check if all nodes in the clique are connected to each other
            if all(b in graph[a] for a, b in combinations(clique, 2)):
                if len(clique) > max_size:
                    max_clique = clique
                    max_size = len(clique)

    return sorted(max_clique)


def generate_password(clique):
    return ",".join(sorted(clique))


def main():
    # Read the network graph
    graph = read_connections("input.txt")

    # Find the largest fully connected set (clique)
    largest_clique = find_largest_clique(graph)

    # Generate the password
    password = generate_password(largest_clique)

    print(f"Password: {password}")


if __name__ == "__main__":
    main()
