def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.read().strip().split('\n')
        # First line contains patterns separated by commas
        patterns = [p.strip() for p in lines[0].split(',')]
        # Skip empty line and get designs
        designs = lines[2:]
    return patterns, designs

def can_make_design(design, patterns):
    if design == '':
        return True
    for pattern in patterns:
        if design.startswith(pattern):
            if can_make_design(design[len(pattern):], patterns):
                return True
    return False

def count_possible_designs(patterns, designs):
    return sum(can_make_design(design, patterns) for design in designs)

def main():
    patterns, designs = read_input('input.txt')
    result = count_possible_designs(patterns, designs)
    print(f"Number of possible designs: {result}")

if __name__ == "__main__":
    main()
