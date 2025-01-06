def perform_shuffle(deck_size, shuffle_type) :
    # Create initial deck
    deck = list(range(deck_size))

    # Keep track of number of shuffles
    shuffles = 0

    # Continue shuffling until we get back to original order
    while True :
        # Perform one shuffle
        shuffles += 1

        # Create new deck for shuffled cards
        new_deck = [0] * deck_size

        if shuffle_type == 'out' :
            # For out-shuffle, first half has (n+1)//2 cards
            first_half_size = (deck_size + 1) // 2
            second_half_size = deck_size // 2

            # InterLeave cards starting with first half
            for i in range(first_half_size) :
                new_deck[i*2] = deck[i]
            for i in range(second_half_size) :
                new_deck[i*2 + 1] = deck[first_half_size + i]

        else :  # in-shuffle
            # For in-shuffle, first half has n//2 cards
            first_half_size = deck_size // 2
            second_half_size = (deck_size + 1) // 2

            # InterLeave cards starting with second half
            for i in range(second_half_size) :
                new_deck[i*2] = deck[first_half_size + i]
            for i in range(first_half_size) :
                new_deck[i*2 + 1] = deck[i]

        # Check if we arer back to original order
        if new_deck == list(range(deck_size)) :
            return shuffles

        # Update deck for next iteration
        deck = new_deck


n, sign =input().split()
n = int(n)

res = perform_shuffle(n, sign)
print(res)