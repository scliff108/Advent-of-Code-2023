DAY = 1
P1_FILENAME = 'input.txt'
P2_FILENAME = 'input.txt'

SPELLED_OUT = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
REVERSED = [i[::-1] for i in SPELLED_OUT]


def part_one(filename):
    with open(filename, 'r') as f:
        total = 0
        for line in f:
            line = line.strip()
            total += get_line_total(line)
    return total


def part_two(filename):
    with open(filename, 'r') as f:
        total = 0
        for line in f:
            line = line.strip()
            # From the front
            line = insert_first_digit(line, SPELLED_OUT)
            # From the back
            line = insert_first_digit(line[::-1], REVERSED)[::-1]
            total += get_line_total(line)
    return total
            

def get_line_total(line):
    first = last = -1

    for char in line:
        if char.isdigit():
            if first < 0: 
                first = int(char)
            last = int(char)

    return first * 10 + last


def insert_first_digit(line, replacements):
    first = len(line)
    # Get the index of each number (string) in the line
    # -1 if the number (string) is not in the line
    idx = [line.find(word) for word in replacements]
    
    # Get the starting index of the first number (string) in the line 
    for i in idx:
        if i >= 0 and i < first:
            first = i

    # Check that we actually found a number (string)
    if first < len(line):
        # Insert the digit of the number (string) just before the word
        i = idx.index(first)
        line = line[:first] + str(i + 1) + line[first:]
    
    return line


def main():

    print('Part 1')
    print(part_one(f'data/day{DAY}/{P1_FILENAME}')) # 54304

    print()
    
    print('Part 2')
    print(part_two(f'data/day{DAY}/{P2_FILENAME}')) # 54418


if __name__ == '__main__':
    main()
