DAY = 4
FILENAME = 'input.txt'

def part_one(lines):
    total = 0
    for line in lines:
        if line > 0:
            total += pow(2, line-1)
    return total

def part_two(lines):
    total = 0
    counts = [1] * len(lines)
    for i in range(len(lines)):
        for j in range(i+1, i+1+lines[i]):
            counts[j] += 1 * counts[i]
    return sum(counts)

def main():
    lines = list()
    with open(f'data/day{DAY}/{FILENAME}', 'r') as f:
        for line in f:
            line = line.strip().split(':')[1].split('|')
            winners = set(line[0].split())
            personal = set(line[1].split())
            line = len(winners.intersection(personal))
            lines.append(line)

    print('Part 1')
    print(part_one(lines)) # 21558

    print()
    
    print('Part 2')
    print(part_two(lines)) # 10425665


if __name__ == '__main__':
    main()
