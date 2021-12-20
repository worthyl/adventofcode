#!/usr/bin/python3
import sys
import itertools
from collections import defaultdict, Counter, deque


def part_one(infile: str):
    SCORES = []
    ans = 0
    for line in open(infile):
        bad = False
        S = deque()
        for c in line.strip():
            if c in ['(', '[', '{', '<']:
                S.append(c)
            elif c==')':
                if S[-1] != '(':
                    ans += 3
                    bad = True
                    break
                else:
                    S.pop()
            elif c==']':
                if S[-1] != '[':
                    ans += 57
                    bad = True
                    break
                else:
                    S.pop()
            elif c=='}':
                if S[-1] != '{':
                    ans += 1197
                    bad = True
                    break
                else:
                    S.pop()
            elif c=='>':
                if S[-1] != '<':
                    ans += 25137
                    bad = True
                    break
                else:
                    S.pop()
        if not bad:
            score = 0
            P = {'(': 1, '[': 2, '{': 3, '<': 4}
            for c in reversed(S):
                score = score*5 + P[c]
            SCORES.append(score)
    print(f'Part one: {ans}')
    return SCORES

def part_two(SCORES: [int]):
    SCORES.sort()
    print(f'Part two: {SCORES[len(SCORES)//2]}')

if __name__ == "__main__":
    input_path = "input.txt"
    part_two(part_one(input_path))