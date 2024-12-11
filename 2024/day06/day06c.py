def solve(infile):
    # Read input once and store as list for faster access
    G = open(infile).read().strip().split('\n')
    R, C = len(G), len(G[0])

    # Find starting position with list comprehension
    sr, sc = next((r, c) for r in range(R) for c in range(C) if G[r][c] == '^')

    # Pre-compute directions
    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def simulate(o_r, o_c):
        r, c = sr, sc
        d = 0  # 0=up, 1=right, 2=down, 3=left
        seen = set()
        seen_rc = set()

        while True:
            state = (r, c, d)
            if state in seen:
                return len(seen_rc), True

            seen.add(state)
            seen_rc.add((r, c))

            dr, dc = DIRS[d]
            rr, cc = r + dr, c + dc

            # Combine boundary checks
            if not (0 <= rr < R and 0 <= cc < C):
                return (len(seen_rc), False) if G[o_r][o_c] == '#' else (0, False)

            if G[rr][cc] == '#' or (rr == o_r and cc == o_c):
                d = (d + 1) % 4
            else:
                r, c = rr, cc

    p1 = p2 = 0
    for o_r in range(R):
        for o_c in range(C):
            result, is_cycle = simulate(o_r, o_c)
            if is_cycle:
                p2 += 1
            else:
                p1 = max(p1, result)

    return p1, p2


if __name__ == '__main__':
    p1, p2 = solve('input.txt')
    # pc.copy(str(p1))
    print(p1)
    # pc.copy(str(p2))
    print(p2)
