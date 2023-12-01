DAY = 0
P1_FILENAME = 'test.txt'
P2_FILENAME = 'test.txt'

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
    print(part_one(f'data/day{DAY}/{P1_FILENAME}'))

    '''
    print()
    
    print('Part 2')
    print(part_two(f'data/day{DAY}/{P2_FILENAME}'))
    '''

if __name__ == '__main__':
    main()
