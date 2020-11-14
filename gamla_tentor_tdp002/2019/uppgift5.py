def create_deck():
    deck = []
    for i in range(1,14):
        for x in ["hearts", "spades", "clubs", "diamonds"]:
            deck.append((i,x))
    return deck

def sort_deck(deck, fun=None):
    if fun:
        return sorted(deck, key=fun)
    else:
        return sorted(deck)
    
deck = create_deck()
deck = sort_deck(deck, lambda x: x[1])

for card in deck:
    print(card)
