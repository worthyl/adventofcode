from pathlib import Path
from collections import namedtuple

State = namedtuple('State', ['a', 'b', 'c', 'i', 'o'])

blocks = Path('input.txt').read_text('utf-8').split('\n\n')
input_program = list(map(int, blocks[1].split()[1].split(',')))
input_state = State(
    *map(lambda r: int(r[2]), map(lambda l: l.split(), blocks[0].splitlines())), 0, None)

def next_out(p: list[int], s: State):
    while s.i < len(p):
        op, ip = p[s.i + 1], s.i + 2
        if (s := State(*[
            lambda: (s.a // (2 ** (s[op & 3] if op & 4 else op)), s.b, s.c, ip, None),
            lambda: (s.a, s.b ^ op, s.c, ip, None),
            lambda: (s.a, (s[op & 3] if op & 4 else op) & 7, s.c, ip, None),
            lambda: (s.a, s.b, s.c, op if s.a else ip, None),
            lambda: (s.a, s.b ^ s.c, s.c, ip, None),
            lambda: (s.a, s.b, s.c, ip, (s[op & 3] if op & 4 else op) & 7),
            lambda: (s.a, s.a // (2 ** (s[op & 3] if op & 4 else op)), s.c, ip, None),
            lambda: (s.a, s.b, s.a // (2 ** (s[op & 3] if op & 4 else op)), ip, None),
        ][p[s.i]]())).o is not None:
            return s

    return s

def forward(program: list[int], s: State) -> str:
    result = []

    while (s := next_out(program, s)).o is not None:
        result.append(s.o)
    return ','.join(map(str, result))

def backward(program: list[int], target: list[int], last: int = 0) -> int:
    for bits in range(8):
        current = last | bits
        if next_out(program, State(current, 0, 0, 0, None)).o != target[-1]:
            continue
        if len(target) == 1 or (current := backward(program, target[:-1], current << 3)) > -1:
            return current
    return -1

print("Part 1:", forward(input_program, input_state))
print("Part_2:", backward(input_program, input_program))