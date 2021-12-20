import math


def part_one(bsearch: str, startbit):
    i = startbit  # index into bs
    tv = int(bsearch[i:i + 3], 2)  # total version
    ID = int(bsearch[i + 3:i + 6], 2)  # packet type ID
    i += 6
    if ID == 4:  # literal value
        while True:
            i += 5
            if bsearch[i - 5] == '0':  # last value packet
                break
    else:
        if bsearch[i] == '0':
            endi = i + 16 + int(bsearch[i + 1:i + 16], 2)
            i += 16
            while i < endi:
                i, v = part_one(bsearch, i)
                tv += v
        else:
            np = int(bsearch[i + 1:i + 12], 2)
            i += 12
            for _ in range(np):
                i, v = part_one(bsearch, i)
                tv += v

    return i, tv


### PART 2 ###

op = [sum, math.prod, min, max,
      lambda ls: ls[0],  # literal
      lambda ls: 1 if ls[0] > ls[1] else 0,  # gt
      lambda ls: 1 if ls[0] < ls[1] else 0,  # lt
      lambda ls: 1 if ls[0] == ls[1] else 0]  # eq


def part_two(bsearch: str, startbit):
    i = startbit  # index into bs
    ID = int(bsearch[i + 3:i + 6], 2)  # packet type ID
    i += 6
    if ID == 4:  # literal value
        vals = [0]
        while True:
            vals[0] = 16 * vals[0] + int(bsearch[i + 1:i + 5], 2)
            i += 5
            if bsearch[i - 5] == '0':  # last value packet
                break
    else:
        vals = []
        if bsearch[i] == '0':  # subpacket length in bits
            endi = i + 16 + int(bsearch[i + 1:i + 16], 2)
            i += 16
            while i < endi:
                i, v = part_two(bsearch, i)
                vals.append(v)
        else:
            np = int(bsearch[i + 1:i + 12], 2)  # number of subpackets
            i += 12
            for _ in range(np):
                i, v = part_two(bsearch, i)
                vals.append(v)

    return i, op[ID](vals)


if __name__ == "__main__":
    input_path = "input.txt"
    bs = bin(int('1' + open("input.txt").read(), 16))[3:]

    print(f'Part one: {part_one(bs, 0)[1]}')
    print(f'Part two: {part_two(bs, 0)[1]}')
