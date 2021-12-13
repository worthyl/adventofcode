lines = []
with open('input.txt', 'r') as file:
    lines = file.readlines()

i = 0
gamma = ""
epsilon = ""

counts = [0,0,0,0,0,0,0,0,0,0,0,0]
with open('input.txt', 'r') as file:
    lines = file.readlines()

n = len(lines)

for line in lines:
    i = 0
    for c in line:
        if c == '1':
            counts[i] += 1
        i += 1

while i < 12:
    if counts[i] > (n / 2): # What if equal?
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
    i += 1

gamma_dec = int(gamma, 2)
epsilon_dec = int(epsilon, 2)

print(f'Part 1 {gamma_dec * epsilon_dec}')