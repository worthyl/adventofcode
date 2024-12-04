import timeit
from collections import Counter

def read_two_lists(filename):
    left_list = []
    right_list = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                # Split the line into values and strip whitespace
                values = line.strip().split()

                # Check if line has exactly two values
                if len(values) == 2:
                    # Convert strings to integers and append to respective lists
                    left_list.append(int(values[0]))
                    right_list.append(int(values[1]))

        return left_list, right_list

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return [], []
    except ValueError:
        print("Error: File contains invalid numeric values")
        return [], []

def calc_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()

    total_distance = 0
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)

    return total_distance

def calculate_similarity_score(left_list, right_list):
    total_score = 0

    # For each number in left list
    for num in left_list:
        # Count how many times it appears in right list
        occurrences = right_list.count(num)
        # Add to total score: number * times it appears
        total_score += num * occurrences

    return total_score

def calc_total_distance2(left, right):
    return sum(abs(l - r) for (l,r) in zip(left, right))

def calculate_similarity_score2(left, right):
    counts = Counter(right)
    return sum(l * counts[l] for l in left)


def main():
    left, right = read_two_lists("input.txt")
    part1 = calc_total_distance2(left, right)
    print(part1)
    #part2 = calculate_similarity_score(left, right)
    part2 = calculate_similarity_score2(left, right)
    print(part2)


if __name__ == "__main__":
    time_taken= timeit.timeit(main, number=1000)
    print(f"Time taken: {time_taken/1000} seconds")

