from collections import defaultdict
import numpy as np


class NetworkAnalyzer:
    def __init__(self):
        self.node_to_idx = None
        self.graph = defaultdict(set)
        self.nodes = []
        self.adj_matrix = None
        self.dp_cache = {}

    def read_connections(self, filename):
        # Read connections and build adjacency sets
        with open(filename, "r") as file:
            for line in file:
                a, b = line.strip().split("-")
                self.graph[a].add(b)
                self.graph[b].add(a)

        # Convert to sorted list of nodes for consistent indexing
        self.nodes = sorted(self.graph.keys())
        self.node_to_idx = {node: idx for idx, node in enumerate(self.nodes)}

        # Create adjacency matrix for faster lookups
        self._build_adjacency_matrix()

    def _build_adjacency_matrix(self):
        n = len(self.nodes)
        self.adj_matrix = np.zeros((n, n), dtype=bool)
        for i, node in enumerate(self.nodes):
            for neighbor in self.graph[node]:
                j = self.node_to_idx[neighbor]
                self.adj_matrix[i, j] = True
                self.adj_matrix[j, i] = True

    def _is_clique(self, vertices):
        # Check if given vertices form a clique using adjacency matrix
        vertex_indices = [self.node_to_idx[v] for v in vertices]
        submatrix = self.adj_matrix[np.ix_(vertex_indices, vertex_indices)]
        return np.all(True == submatrix) - np.all(np.eye(len(vertices), dtype=bool))

    def find_max_clique_dp(self):
        def get_candidates(current_clique, excluded):
            # Get potential candidates that could extend the current clique
            if not current_clique:
                return set(self.nodes)

            # Find nodes connected to all nodes in current clique
            candidates = set.intersection(*(self.graph[v] for v in current_clique))
            candidates -= excluded
            return candidates

        def extend_clique(current_clique, excluded):
            # Check cache
            key = (tuple(sorted(current_clique)), tuple(sorted(excluded)))
            if key in self.dp_cache:
                return self.dp_cache[key]

            # Base case: no more candidates
            candidates = get_candidates(current_clique, excluded)
            if not candidates:
                return current_clique

            max_clique = current_clique

            # Try extending with each candidate
            for vertex in sorted(
                candidates, key=lambda x: len(self.graph[x]), reverse=True
            ):
                new_clique = extend_clique(
                    current_clique | {vertex},
                    excluded | {v for v in candidates if v < vertex},
                )
                if len(new_clique) > len(max_clique):
                    max_clique = new_clique

            # Cache and return result
            self.dp_cache[key] = max_clique
            return max_clique

        return extend_clique(set(), set())

    def generate_password(self, clique):
        return ",".join(sorted(clique))


def main():
    analyzer = NetworkAnalyzer()
    analyzer.read_connections("input.txt")

    # Find largest clique using dynamic programming
    largest_clique = analyzer.find_max_clique_dp()

    # Generate password
    password = analyzer.generate_password(largest_clique)
    print(f"Password: {password}")
    print(f"Clique size: {len(largest_clique)}")


if __name__ == "__main__":
    main()
