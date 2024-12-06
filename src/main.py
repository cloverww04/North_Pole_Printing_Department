import os
from collections import defaultdict

def parse_file(filepath):
    """Reads the file and returns both dependency rules and rows."""
    dependencies = defaultdict(set)
    rows = []

    try:
        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines
                
                if line.startswith("#"):
                    continue
                
                if "|" in line:
                    left, right = line.split('|')
                    dependencies[right].add(left)
                else:
                    rows.append(line.split(','))
                    
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None, None

    return dependencies, rows

def validate_row(row, dependencies):
    """Checks if a row satisfies the dependency rules."""
    seen = set()
    for number in row:
        if number in dependencies:
            for dependency in dependencies[number]:
                if dependency in row and dependency not in seen:
                    print(f"Dependency {dependency} for {number} not met in row {row}")
                    return False
        seen.add(number)
    return True

def process_numbers(rows, dependencies):
    """Processes rows, keeping only those that satisfy the dependencies."""
    valid_rows = []
    for row in rows:
        print(f'Checking row: {row}')
        if validate_row(row, dependencies):
            valid_rows.append(row)
            print(f'Row is valid: {row}')
        else:
            print(f"Skipping invalid row: {row}")
    return valid_rows

def sum_middle_numbers(valid_rows):
    """Calculates the sum of the middle numbers from each valid row."""
    total_sum = 0
    for row in valid_rows:
        middle_index = len(row) // 2
        middle_number = int(row[middle_index])  # Convert to integer
        total_sum += middle_number
    return total_sum

def main():

    file_path = "ruleset.txt"
    
    dependencies, rows = parse_file(file_path)
    if not dependencies or not rows:
        return

    valid_rows = process_numbers(rows, dependencies)

    print("Valid Rows:")
    for row in valid_rows:
        print(row)

    # Calculate the total sum of middle numbers from valid rows
    total_sum = sum_middle_numbers(valid_rows)
    print(f"Total sum of middle numbers: {total_sum}")

if __name__ == "__main__":
    main()