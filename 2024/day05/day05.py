from collections import deque
from typing import Any

# Example input
example_rules = [
    "47|53",
    "97|13",
    "97|61",
    "97|47",
    "75|29",
    "61|13",
    "75|53",
    "29|13",
    "97|29",
    "53|29",
    "61|53",
    "97|53",
    "61|29",
    "47|13",
    "75|47",
    "97|75",
    "47|61",
    "75|61",
    "47|29",
    "75|13",
    "53|13"
]

example_updates = [
    "75,47,61,53,29",
    "97,61,53,29,13",
    "75,29,13",
    "75,97,47,61,53",
    "61,13,29",
    "97,13,75,29,47"
]


def build_graph(rules):
    graph = {}
    for rule in rules:
        x, y = map(int, rule.split('|'))
        if x not in graph:
            graph[x] = set()
        graph[x].add(y)
    return graph


def is_valid_order(pages, graph):
    seen = set()
    for i, page in enumerate(pages):
        seen.add(page)
        if page in graph:
            for next_page in graph[page]:
                if next_page in pages[i + 1:]:
                    continue
                if next_page in pages[:i]:
                    return False
        for prev_page, next_pages in graph.items():
            if page in next_pages and prev_page in pages[i:]:
                return False
    return True


def get_middle_number(pages):
    return pages[len(pages) // 2]


def find_invalid_updates(rules, updates):
    graph = build_graph(rules)
    invalid_updates = []
    for update in updates:
        pages = list(map(int, update.split(',')))
        if not is_valid_order(pages, graph):
            invalid_updates.append(pages)
    return invalid_updates


def topological_sort(graph, pages):
    # Create a subgraph with only the pages we care about
    pages_set = set(pages)
    in_degree = {page: 0 for page in pages}

    # Calculate in-degrees
    for page in pages:
        if page in graph:
            for neighbor in graph[page]:
                if neighbor in pages_set:
                    in_degree[neighbor] += 1

    # Find all nodes with in-degree 0
    queue = deque([page for page in pages if in_degree[page] == 0])
    result: list[Any] = []

    while queue:
        current = queue.popleft()
        result.append(current)

        if current in graph:
            for neighbor in graph[current]:
                if neighbor in pages_set:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

    return result if len(result) == len(pages) else []


def solve_part1(rules, updates):
    graph = build_graph(rules)
    total = 0
    for update in updates:
        pages = list(map(int, update.split(',')))
        if is_valid_order(pages, graph):
            middle = get_middle_number(pages)
            # print(f"Valid update: {pages}, middle number: {middle}")
            total += middle
    return total


def solve_part2(rules, updates):
    graph = build_graph(rules)
    invalid_updates = find_invalid_updates(rules, updates)
    total = 0

    # print("\nProcessing invalid updates:")
    for pages in invalid_updates:
        # print(f"Original invalid update: {pages}")
        reordered = topological_sort(graph, pages)
        middle = get_middle_number(reordered)
        # print(f"Reordered: {reordered}, middle number: {middle}")
        total += middle

    return total


def example():
    # Convert string updates to lists of integers
    updates = [list(map(int, update.split(','))) for update in example_updates]

    print("Solving Part 1...")
    result1 = solve_part1(example_rules, example_updates)
    print(f"Part 1 result: {result1}")

    print("\nSolving Part 2...")
    result2 = solve_part2(example_rules, example_updates)
    print(f"Part 2 result: {result2}")


def actual():
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
        # Find the empty line that separates rules from updates
        separator = lines.index('')
        rules = lines[:separator]
        updates = lines[separator + 1:]

        print("\nSolving actual input...")
        result1 = solve_part1(rules, updates)
        print(f"Part 1 result: {result1}")

        result2 = solve_part2(rules, updates)
        print(f"Part 2 result: {result2}")


def main():
    actual()


if __name__ == "__main__":
    main()
