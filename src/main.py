from functools import cmp_to_key

# Function to load rules from a file
def load_rules(filename):
    rules = []
    with open(filename, 'r') as file:
        for line in file:
            a, b = map(int, line.strip().split('|'))
            rules.append((a, b))
    return rules

# Function to load data from a file
def load_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            row = tuple(map(int, line.strip().split(',')))
            data.append(row)
    return data

# Load the rules and data
rules = load_rules('rules.txt')
data = load_data('data.txt')

# Create a precedence dictionary
precedence = {}
for a, b in rules:
    if a not in precedence:
        precedence[a] = set()
    precedence[a].add(b)

# compare two numbers based on the rules
def compare(a, b):
    if a in precedence and b in precedence[a]:
        return -1
    elif b in precedence and a in precedence[b]:
        return 1
    return 0

# Sort the data 
sorted_data_with_flags = []
invalid_list = []
for row in data:
    sorted_row = sorted(row, key=cmp_to_key(compare))
    flag = sorted_row != list(row) 
    sorted_data_with_flags.append((sorted_row, flag))

# Output the sorted data with flags and store the invalid rows
for row, flag in sorted_data_with_flags:
    if flag: 
        invalid_list.append(row)

# Calculate middle page numbers
totalSum = 0
for row in invalid_list:
    middle_index = len(row) // 2
    middle_number = row[middle_index]
    totalSum += middle_number
    
print(f"Total: {totalSum}")
