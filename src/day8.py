DAY = 8
FILENAME = 'input.txt'


def part_one(instructions, data):
    instruction_len = len(instructions)
    step = 0
    curr = 'AAA'
    while curr != 'ZZZ':
        i = 1 if instructions[step % instruction_len] == 'R' else 0
        curr = data[curr][i]
        step += 1
    return step


def ends_with_A(data):
    res = list()
    for key in data.keys():
        if key[-1].endswith('A'):
            res.append(key)
    return res


def part_two(instructions, data):
    instruction_len = len(instructions)
    step = 0
    curr = ends_with_A(data)
    flag = False
    while not flag:
        flag = True
        for idx, c in enumerate(curr):
            i = 1 if instructions[step % instruction_len] == 'R' else 0
            curr[idx] = data[c][i]
            if flag and not data[c][i].endswith('Z'):
                flag = False
        step += 1
    return step


def main():
    data = dict()
    with open(f'data/day{DAY}/{FILENAME}', 'r') as f:
        instructions = f.readline().strip()
        f.readline()
        for line in f:
            line = line.strip().split(' = ')
            data[line[0]] = line[1][1:-1].split(', ')

    # print('Part 1')
    # print(part_one(instructions, data))

    # print()
    
    print('Part 2')
    print(part_two(instructions, data))


if __name__ == '__main__':
    main()
