def is_safe(report):
    # Calculate differences between adjacent numbers
    differences = [b - a for a, b in zip(report, report[1:])]
    # Check if differences are within valid range for increasing/decreasing
    increasing = all(1 <= diff <= 3 for diff in differences)
    decreasing = all(-3 <= diff <= -1 for diff in differences)
    return increasing or decreasing

def check_safety(filename):
    # Read the file and convert each line to a list of integers
    with open(filename, 'r') as file:
        reports = [list(map(int, line.split())) for line in file.readlines()]

    # Count safe reports
    safety_checks = [is_safe(report) for report in reports]
    return sum(safety_checks)

def check_safety_with_dampeners(filename):

    # Read the file and convert each line to a list of integers
    with open(filename, 'r') as file:
        reports = [list(map(int, line.split())) for line in file.readlines()]

    def is_safe_with_dampener(report):
        # If the report is already safe
        if is_safe(report):
            return True
        # Try removing each level and check if the remaining is safe
        for i in range(len(report)):
            if is_safe(report[:i] + report[i+1:]):
                return True
        return False

    # Count safe reports with dampener
    safety_checks = [is_safe_with_dampener(report) for report in reports]
    return sum(safety_checks)


# Example usage
filename = "input.txt"
safe_count = check_safety(filename)
print(f"Number of safe reports: {safe_count}")
safe_count = check_safety_with_dampeners(filename)
print(f"Number of safe reports with dampeners: {safe_count}")
