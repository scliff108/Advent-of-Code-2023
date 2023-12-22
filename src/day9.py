DAY = 9
FILENAME = 'input.txt'


def part_one(data):
    result = 0
    for row in data:
        values = get_deltas(row, [row[-1]])
        result += predict(values)
    return result


def get_deltas(row, values, idx=-1):
    deltas = [row[i] - row[i-1] for i in range(1, len(row))]
    values.append(deltas[idx])
    if all(d == 0 for d in deltas):
        return values
    return get_deltas(deltas, values, idx)


def predict(values):
    while len(values) >= 2:
        values[-2] = values[-1] + values[-2]
        del values[-1]
    return values[0]


def part_two(data):
    result = 0
    for row in data:
        values = get_deltas(row, [row[0]], 0)
        prediction = predict2(values)
        result += prediction
    return result


def predict2(values):
    while len(values) >= 2:
        values[-2] = values[-2] - values[-1]
        del values[-1]
    return values[0]


def main():
    filename = f'data/day{DAY}/{FILENAME}'
    with open(filename, 'r') as f:
        data = [[int(i) for i in line.strip().split()] for line in f]

    print('Part 1')
    print(part_one(data))

    print()
    
    print('Part 2')
    print(part_two(data))


if __name__ == '__main__':
    main()
