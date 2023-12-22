DAY = 0
FILENAME = 'test.txt'


def part_one(filename):
    with open(filename, 'r') as f:
        for line in f:
            print(line)
    return ''


def part_two(filename):
    with open(filename, 'r') as f:
        for line in f:
            print(line)
    return ''


def main():

    print('Part 1')
    print(part_one(f'data/day{DAY}/{FILENAME}'))

    '''
    print()
    
    print('Part 2')
    print(part_two(f'data/day{DAY}/{FILENAME}'))
    '''


if __name__ == '__main__':
    main()
