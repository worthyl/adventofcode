import sys
import re
import numpy as np
import timeit

def main():
    from collections import defaultdict, Counter
    # D = open(sys.argv[1]).read().strip()
    # L = D.split('\n')

    data_matrix = np.loadtxt("input.txt", dtype=int)
    col_1 = data_matrix[:, 0]
    col_2 = data_matrix[:, 1]

    result = 0
    # PART2
    for i, val in enumerate(col_1):
        col_2_uni, col_2_cnts = np.unique(col_2, return_counts=True)
        if val not in col_2_uni:
            continue
        result += val * col_2_cnts[col_2_uni == val]

    print("Part 2 Results:", result)

    result = 0
    # PART 1
    while len(col_1) > 0:
        min_col1 = col_1[np.argmin(col_1)]
        min_col2 = col_2[np.argmin(col_2)]
        result += np.abs(min_col1 - min_col2)
        col_1 = np.delete(col_1, np.argmin(col_1))
        col_2 = np.delete(col_2, np.argmin(col_2))

    print("Part 1 Results:", result)

if __name__ == "__main__":
    time_taken= timeit.timeit(main, number=1000)
    print(f"Time taken: {time_taken/1000} seconds")