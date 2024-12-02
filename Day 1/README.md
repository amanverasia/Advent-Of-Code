# Day 1: Historian Hysteria

## Problem Description

The Chief Historian has gone missing, and the Senior Historians need help finding him! They've discovered two lists of location IDs in his office, but the lists don't quite match up.

### Part 1: Distance Between Lists

Compare two lists of location IDs by:
1. Sorting both lists
2. Pairing up numbers (smallest with smallest, second-smallest with second-smallest, etc.)
3. Calculating the absolute difference between each pair
4. Summing up all the differences

#### Example
```
Left List  Right List  |Difference|
    1         3           2
    2         3           1
    3         3           0
    3         4           1
    3         5           2
    4         9           5
                Total:   11
```

### Part 2: Similarity Score

Calculate how similar the lists are by:
1. For each number in the left list:
   - Count how many times it appears in the right list
   - Multiply the number by its count in the right list
2. Sum up all these products

#### Example
```
Left List: 3,4,2,1,3,3
Right List: 4,3,5,3,9,3

3 appears 3 times in right list: 3 * 3 = 9
4 appears 1 time in right list:  4 * 1 = 4
2 appears 0 times in right list: 2 * 0 = 0
1 appears 0 times in right list: 1 * 0 = 0
3 appears 3 times in right list: 3 * 3 = 9
3 appears 3 times in right list: 3 * 3 = 9
                         Total Score: 31
```

## Solutions

- Part 1: 3714264
- Part 2: 18805872

## Implementation Notes

The solution uses Python to:
- Parse input by splitting each line into left and right columns
- Sort both lists for part 1 comparison
- Use list counting methods for part 2 similarity calculation

## Running the Solution

```bash
python solution.py
```

## Input Format

Each line contains two numbers separated by spaces:
```
left_number   right_number
```