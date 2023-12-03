DAY = 3
FILENAME = 'input.txt'

NOT_SYMBOLS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']


def part_one(lines):
    total = 0
    for i in range(len(lines)):
        num_list = process_line(lines[i])
        for num_tuple in num_list:
            total += check_neighbors(lines, i, num_tuple)

    return total


def part_two(lines):
    total = 0
    lines_list = list()
    for i in range(len(lines)):
        lines[i] = list(lines[i])
        process_line2(lines[i])
    for i in range(len(lines)):
        total += check_neighbors2(lines, i)
    return total


def process_line(line):
    nums_in_line = list()
    i = 0
    num_bool = False
    num_str = ''
    start = 0
    
    while i < len(line):
        if line[i].isdigit():
            if not num_bool:
                start = i
                num_bool = True
            num_str += line[i]
        elif num_bool:
            nums_in_line.append((num_str, start))
            num_str = ''
            num_bool = False
        i += 1
    if num_bool:
        nums_in_line.append((num_str, start))
        num_str = ''
        num_bool = False
        
    return nums_in_line


def check_neighbors(lines, line_num, num_tuple):
    num_len = len(num_tuple[0])
    num = int(num_tuple[0])
    start = num_tuple[1]
    look_left = look_right = look_up = look_down = False

    if start > 0:
        # Look left
        look_left = True
        
    if start + num_len < len(lines[line_num]):
        # Look right
        look_right = True
        if lines[line_num][start+num_len] not in NOT_SYMBOLS:
            return num
    if line_num != 0:
        # Look up
        look_up = True
    if line_num != len(lines) - 1:
        look_down = True
    
    if look_left:
        if lines[line_num][start-1] not in NOT_SYMBOLS:
            return num
        if look_up and lines[line_num-1][start-1] not in NOT_SYMBOLS:
            return num
        if look_down and lines[line_num+1][start-1] not in NOT_SYMBOLS:
            return num
    
    if look_right:
        if lines[line_num][start+num_len] not in NOT_SYMBOLS:
            return num
        if look_up and lines[line_num-1][start+num_len] not in NOT_SYMBOLS:
            return num
        if look_down and lines[line_num+1][start+num_len] not in NOT_SYMBOLS:
            return num

    for i in range(start, start+num_len):
        if look_up and lines[line_num-1][i] not in NOT_SYMBOLS:
            return num
        if look_down and lines[line_num+1][i] not in NOT_SYMBOLS:
            return num
    
    return 0


def process_line2(line):
    i = 0
    num_bool = False
    num_str = ''
    start = 0
    
    while i < len(line):
        if line[i].isdigit():
            if not num_bool:
                start = i
                num_bool = True
            num_str += line[i]
        elif num_bool:
            for j in range(start, i):
                line[j] = int(num_str)
            num_str = ''
            num_bool = False
        i += 1
    if num_bool:
        for j in range(start, i):
            line[j] = int(num_str)
        num_str = ''
        num_bool = False
        

def check_neighbors2(lines, n):
    total = 0
    start = 0
    while '*' in lines[n]:
        start = lines[n].index('*')

        look_left = look_right = look_up = look_down = False

        if start > 0:
            look_left = True
        if start < len(lines[n]) - 1:
            look_right = True
        if n != 0:
            look_up = True
        if n != len(lines) - 1:
            look_down = True

        # [
        #     [0 1 2]
        #     [3 * 4]
        #     [5 6 7]
        # ]
        neighbors = ['.'] * 8

        neighbors[0] = lines[n-1][start-1] if look_up and look_left else '.'
        neighbors[1] = lines[n-1][start] if look_up else '.'
        neighbors[2] = lines[n-1][start+1] if look_up and look_right else '.'
        neighbors[3] = lines[n][start-1] if look_left else '.'
        neighbors[4] = lines[n][start+1] if look_right else '.'
        neighbors[5] = lines[n+1][start-1] if look_down and look_left else '.'
        neighbors[6] = lines[n+1][start] if look_down else '.'
        neighbors[7] = lines[n+1][start+1] if look_down and look_right else '.'


        neighbors = list(filter(lambda x : not isinstance(x, str), neighbors))
        n_set = set(neighbors)
        print(n_set)
        if len(n_set) == 2:
            total += 1 * n_set.pop() * n_set.pop()

        lines[n][start] = '.'
            
    return total


def main():
    filename = f'data/day{DAY}/{FILENAME}'

    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]

    print('Part 1')
    print(part_one(lines)) # 550064

    print()
    
    print('Part 2')
    print(part_two(lines)) # 85010461

if __name__ == '__main__':
    main()
