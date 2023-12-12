import sys

DAY = 5
FILENAME = 'test.txt'
TITLES = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light',
          'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']

def get_next(data, current):
    for d in data:
        dest = d[0]
        source = d[1]
        range_length = d[2]
        if current >= source and current < source + range_length:
            return current - source + dest
    return current


def part_one(data):
    best = sys.maxsize
    seeds = data['seeds']
    for seed in seeds:
        current = seed
        for title in TITLES:
            current = get_next(data[title], current)
        best = current if current < best else best
    return best


def get_data(filename):
    data = dict()
    with open(filename, 'r') as f:
        data['seeds'] = [int(i) for i in f.readline().split(': ')[1].split()]
        f.readline()
        for i in range(7):
            line = f.readline().strip()
            source_dest = line.split()[0]
            data[source_dest] = list()
            while True:
                line = f.readline().strip()
                if not line:
                    break
                mapping_data = [int(i) for i in line.split()]
                data[source_dest].append(mapping_data)
    return data


def main():

    data = get_data(f'data/day{DAY}/{FILENAME}')

    print('Part 1')
    print(part_one(data))

    # print()
    
    # print('Part 2')
    # print(part_two(data))

if __name__ == '__main__':
    main()
