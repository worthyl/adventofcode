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


def find_connected_triples(graph):
    # Get all nodes
    nodes = list(graph.keys())
    triples = []

    # Check all possible combinations of three nodes
    for a, b, c in combinations(nodes, 3):
        # Check if all three nodes are connected to each other
        if b in graph[a] and c in graph[a] and c in graph[b]:
            triples.append(sorted([a, b, c]))

    return triples


def count_t_triples(triples):
    # Count triples containing at least one node starting with 't'
    t_count = 0
    t_triples = []

    for triple in triples:
        if any(node.startswith("t") for node in triple):
            t_count += 1
            t_triples.append(",".join(triple))

    return t_count, t_triples


def main():
    # Read the network graph
    graph = read_connections("input.txt")

    # Find all connected triples
    triples = find_connected_triples(graph)

    # Count triples with 't' computers
    t_count, t_triples = count_t_triples(triples)

    print(f"Total triples with 't' computers: {t_count}")
    print("\nTriples containing 't' computers:")

    for triple in t_triples:
        print(triple)


if __name__ == "__main__":
    main()
