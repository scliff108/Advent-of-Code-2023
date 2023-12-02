DAY = 2
FILENAME = 'input.txt'

RED = 'red'
GREEN = 'green'
BLUE = 'blue'
ROCK_DICT = {RED: 0, GREEN: 0, BLUE: 0}
CONSTRAINTS = {RED: 12, GREEN: 13, BLUE: 14}

def part_one(games: dict):
    all_games = set(games.keys())
    impossible = set()
    for game in games.keys():
        for round in games[game]:
            if ((round[RED] > CONSTRAINTS[RED]) or
               (round[GREEN] > CONSTRAINTS[GREEN]) or
               (round[BLUE] > CONSTRAINTS[BLUE])):
                impossible.add(game)
                break
        else:
            continue
    possible = all_games.difference(impossible)
    return sum(possible)


def part_two(games: dict):
    total = 0
    for game in games.keys():
        max_red = max_green = max_blue = 0
        for round in games[game]:
            max_red = max_red if max_red >= round[RED] else round[RED]
            max_green = max_green if max_green >= round[GREEN] else round[GREEN]
            max_blue = max_blue if max_blue >= round[BLUE] else round[BLUE]
        total += max_red * max_green * max_blue
    return total


def get_games(filename):
    games = dict()
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            game, data = line.split(': ')
            game = int(game.split()[1])
            games[game] = list()

            rounds = data.split(';')
            for round in rounds:
                games[game].append(ROCK_DICT.copy())
                rocks = round.split(', ')
                for rock in rocks:
                    count, color = rock.split()
                    games[game][-1][color] = int(count)
    return games


def main():
    games = get_games(f'data/day{DAY}/{FILENAME}')
    print('Part 1')
    print(part_one(games)) # 2727

    print()
    
    print('Part 2')
    print(part_two(games)) # 56580


if __name__ == '__main__':
    main()
