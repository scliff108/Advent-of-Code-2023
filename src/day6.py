DAY = 6
FILENAME = 'input.txt'


def get_result(wins):
    total = 1
    for w in wins:
        total *= w
    return total


def part_one(data):
    all_wins = list()
    for d in data:
        wins = 0
        time, distance = d
        for v in range(time):
            x = v * (time - v)
            if x > distance:
                wins += 1
        all_wins.append(wins)
    return get_result(all_wins)


def part_two(time, distance):
    min_time = 0
    while min_time * (time - min_time) < distance:
        min_time += 1

    max_time = time
    while max_time * (time - max_time) < distance:
        max_time -= 1

    return max_time - min_time + 1


def main():
    with open(f'data/day{DAY}/{FILENAME}', 'r') as f:
        times = f.readline()
        distances = f.readline()
        times = [int(t) for t in times.split()[1:]]
        distances = [int(d) for d in distances.split()[1:]]
    
    data = list(zip(times, distances))

    print('Part 1')
    print(part_one(data))

    print()

    with open(f'data/day{DAY}/{FILENAME}', 'r') as f:
        times = f.readline()
        distances = f.readline()
        times = times.split(':')[1]
        distances = distances.split(':')[1]  
        time = int(times.replace(' ', ''))
        distance = int(distances.replace(' ', ''))

    print('Part 2')
    print(part_two(time, distance))


if __name__ == '__main__':
    main()
