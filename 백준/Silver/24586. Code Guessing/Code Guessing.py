def sol_24586() :
    p, q = map(int, input().split())
    pattern = input().rstrip()

    all_cards = set(range(1, 10))
    remaining_cards = list(all_cards - {p, q})

    valid_pairs = []

    for x in range(len(remaining_cards) - 1) :
        for y in range(x + 1, len(remaining_cards)) :
            cards = sorted([p, q, remaining_cards[x], remaining_cards[y]])

            generated_pattern = ''.join('A' if card in (p, q) else 'B' for card in cards)

            if generated_pattern == pattern :
                valid_pairs.append(tuple(sorted((remaining_cards[x], remaining_cards[y]))))

    if len(valid_pairs) == 1 :
        print(valid_pairs[0][0], valid_pairs[0][1])
    else :
        print(-1)



sol_24586()