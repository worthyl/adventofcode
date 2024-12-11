import sys
import re
from collections import defaultdict, Counter, deque
import pyperclip as pc

# Increase recursion limit and setup input
sys.setrecursionlimit(10 ** 6)
infile = 'input.txt'


# Helper function to print and copy result
def pr(s):
    print(s)
    pc.copy(s)


# Read input data
D = open(infile).read().strip()


def solve(part2):
    # Initialize data structures
    A = deque([])  # Stores file positions and sizes
    SPACE = deque([])  # Stores empty space positions and sizes
    FINAL = []  # Final arrangement of files
    pos = 0  # Current position tracker
    file_id = 0  # File identifier

    # Parse input and build initial arrangement
    for i, c in enumerate(D):
        if i % 2 == 0:  # File entries
            if part2:
                A.append((pos, int(c), file_id))
            else:
                # Split files into unit sizes for part 1
                for _ in range(int(c)):
                    A.append((pos, 1, file_id))
                    FINAL.append(file_id)
                    pos += 1

            if part2:
                for _ in range(int(c)):
                    FINAL.append(file_id)
                    pos += 1
            file_id += 1
        else:  # Space entries
            SPACE.append((pos, int(c)))
            for _ in range(int(c)):
                FINAL.append(None)
                pos += 1

    # Process files in reverse order
    for pos, sz, file_id in reversed(A):
        # Find suitable space for each file
        for space_i, (space_pos, space_sz) in enumerate(SPACE):
            if space_pos < pos and sz <= space_sz:
                # Move file to new position
                for i in range(sz):
                    assert FINAL[pos + i] == file_id, f'{FINAL[pos+i]=}'
                    FINAL[pos + i] = None
                    FINAL[space_pos + i] = file_id
                # Update available space
                SPACE[space_i] = (space_pos + sz, space_sz - sz)
                break

    # Calculate final score
    ans = sum(i * c for i, c in enumerate(FINAL) if c is not None)
    return ans


# Solve both parts
p1 = solve(False)
p2 = solve(True)

# Output results
pr(p1)
pr(p2)
