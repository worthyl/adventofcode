def create_boards(lines):
    i = 2  # line of first board
    boards = []
    while i < len(lines):
        board = {'rows': [], 'marks': [], 'has_won': False}
        while i < len(lines) and lines[i] != '':
            line = lines[i]
            row = [int(n.strip()) for n in line.split()]
            board['rows'].append(row)
            board['marks'].append([False, False, False, False, False])

            i += 1
        boards.append(board)
        i += 1
    return boards


def update(board, nbr):
    marks = board['marks']
    rows = board['rows']
    i = 0
    while i < len(rows):
        j = 0
        row = rows[i]
        while j < len(row):
            if nbr == row[j]:
                marks[i][j] = True
            j += 1
        i += 1


def has_won(board):
    marks = board['marks']
    rows = board['rows']
    if [True, True, True, True, True] in marks:
        return True
    i = 0
    while i < len(rows):
        j = 0
        all_checked = True
        while j < len(rows[0]):
            if not marks[j][i]:
                all_checked = False
            j += 1
        if all_checked:
            return True
        i += 1
    return False


def calculate_score(board, last_nbr):
    marks = board['marks']
    rows = board['rows']
    total = 0
    i = 0
    while i < len(rows):
        j = 0
        while j < len(rows[0]):
            if not marks[i][j]:
                total += rows[i][j]
            j += 1
        i += 1
    return total * last_nbr


def part_one(board_lines: list[str], nbrs: list[int]):
    boards = create_boards(board_lines)

    for nbr in nbrs:
        for board in boards:
            update(board, nbr)
            if has_won(board):
                print(f'Part 1: {calculate_score(board, nbr)}')
                return


def part_two(board_lines: list[str], nbrs: list[int]):
    boards = create_boards(board_lines)

    nbr_won = 0
    for nbr in nbrs:
        for board in boards:
            if not board['has_won']:
                update(board, nbr)
                if has_won(board):
                    board['has_won'] = True
                    nbr_won += 1
                    if nbr_won == len(boards):
                        print(f'Part 2: {calculate_score(board, nbr)}')
                        return


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        lines = [l.strip() for l in file.readlines()]

    nbrs = [int(n) for n in lines[0].split(",")]
    part_one(lines, nbrs)
    part_two(lines, nbrs)
