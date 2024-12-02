def parse_input(filename):
    """
    Read and parse the input file.
    Returns two lists containing left and right columns.
    """
    data = []
    with open(filename, "r") as f:
        data = [line.rstrip("\n") for line in f.readlines()]
    
    l_column = []
    r_column = []
    for line in data:
        l_column.append(line.split(" ")[0])
        r_column.append(line.split(" ")[3])
    
    return l_column, r_column

def solve_part1(l_column, r_column):
    """
    Calculate the sum of absolute differences between sorted columns.
    """
    l_sorted = sorted(l_column)
    r_sorted = sorted(r_column)
    
    return sum(abs(int(l) - int(r)) for l, r in zip(l_sorted, r_sorted))

def solve_part2(l_column, r_column):
    """
    Calculate similarity score based on matching numbers and their frequency.
    """
    l_sorted = sorted(l_column)
    r_sorted = sorted(r_column)
    
    similarity_score = 0
    for num in l_sorted:
        if num in r_sorted:
            similarity_score += (int(num) * r_sorted.count(num))
    
    return similarity_score

def main():
    input_file = "Day 1/input.txt"
    l_column, r_column = parse_input(input_file)
    
    # Solve Part 1
    part1_result = solve_part1(l_column, r_column)
    print(f"Part 1: {part1_result}")
    
    # Solve Part 2
    part2_result = solve_part2(l_column, r_column)
    print(f"Part 2: {part2_result}")

if __name__ == "__main__":
    main()