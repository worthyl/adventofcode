def generate_secret_numbers(initial_secret, steps=2000):
    secret = initial_secret
    for _ in range(steps):
        # Step 1: Multiply by 64, mix, prune
        secret = (secret ^ (secret * 64)) % 16777216
        # Step 2: Divide by 32, mix, prune
        secret = (secret ^ (secret // 32)) % 16777216
        # Step 3: Multiply by 2048, mix, prune
        secret = (secret ^ (secret * 2048)) % 16777216
    return secret

def process_input_file(filename):
    with open(filename, 'r') as file:
        initial_secrets = [int(line.strip()) for line in file]
    results = {initial: generate_secret_numbers(initial) for initial in initial_secrets}
    return sum(results.values())

def main():
    filename = 'input.txt'
    result = process_input_file(filename)
    print(result)


if __name__ == '__main__':
    main()
