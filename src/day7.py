from functools import cmp_to_key

DAY = 7
FILENAME = 'input.txt'
CARD_RANK = '23456789TJQKA'
CARD_RANK2 = 'J23456789TQKA'

def hand_type(hand):
    hand_set = list(set(hand))
    vals = [(hand.count(h), CARD_RANK.index(h)) for h in hand_set]
    vals = sorted(vals, key=lambda x: (x[0], x[1]), reverse=True)
    l = len(hand_set)

    if l == 1:
        return 0, vals
    
    if l == 2:
        if vals[0][0] == 4:
            # 4 of a kind
            return 1, vals
        # Full house
        return 2, vals
    
    if l == 3:
        if vals[0][0] == 3:
            # 3 of a kind
            return 3, vals
        # 2 pair
        return 4, vals
    
    if l == 4:
        # 1 pair
        return 5, vals

    # High card
    return 6, vals


def hand_type2(hand):
    joker_count = hand.count('J')
    rank, cards = hand_type(hand)
    
    if joker_count == 0 or joker_count == 5:
        # No impact, 5 of a kind
        return rank, cards
    if rank == 1 and joker_count == 1 or rank == 1 and joker_count == 4:
        # 4 of a kind to 5 of a kind
        return 0, cards
    if rank == 2 and joker_count == 2 or rank == 2 and joker_count == 3:
        # Full house to 5 of a kind
        return 0, cards
    if rank == 3:
        # 3 of a kind to 4 of a kind
        return 1, cards
    if rank == 4 and joker_count == 2:
        # 2 pairs to 4 of a kind
        return 1, cards
    if rank == 4:
        # 2 pairs to full house
        return 2, cards
    if rank == 5:
        # 1 pair to 3 of a kind
        return 3, cards
    # High card to pair
    return 5, cards


def compare_hands(x, y):
    if x['rank'] != y['rank']:
        return 1 if x['rank'] < y['rank'] else -1
    
    for i in range(len(x['hand'])):
        if x['hand'][i] != y['hand'][i]:
            return 1 if CARD_RANK.index(x['hand'][i]) > CARD_RANK.index(y['hand'][i]) else -1
    
    return 0


def compare_hands2(x, y):
    if x['rank'] != y['rank']:
        return 1 if x['rank'] < y['rank'] else -1
    
    for i in range(len(x['hand'])):
        if x['hand'][i] != y['hand'][i]:
            return 1 if CARD_RANK2.index(x['hand'][i]) > CARD_RANK2.index(y['hand'][i]) else -1
    
    return 0


def part_one(data):
    data = sorted(data, key=cmp_to_key(compare_hands))
    total = 0
    for idx, d in enumerate(data, 1):
        total += d.get('bid') * idx
    return total


def part_two(data):
    data = sorted(data, key=cmp_to_key(compare_hands2))
    total = 0
    for idx, d in enumerate(data, 1):
        total += d.get('bid') * idx
    return total
    return ''


def main():
    data = list()
    with open(f'data/day{DAY}/{FILENAME}', 'r') as f:
        for line in f:
            hand, bid = line.split()
            rank, cards = hand_type(hand)
            data.append({
                'hand': hand,
                'bid': int(bid),
                'rank': rank,
                'cards': cards,
            })

    print('Part 1')
    print(part_one(data))

    print()

    data2 = list()
    with open(f'data/day{DAY}/{FILENAME}', 'r') as f:
        for line in f:
            hand, bid = line.split()
            rank, cards = hand_type2(hand)
            data2.append({
                'hand': hand,
                'bid': int(bid),
                'rank': rank,
                'cards': cards,
            })
    
    print('Part 2')
    print(part_two(data2))


if __name__ == '__main__':
    main()
