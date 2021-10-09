from game import Deck, Player

deck = Deck()


print(deck)

player = Player("Dan", deck=deck)

player.shuffle()
print(deck)

for i in range(52):
    print("length", len(deck))
    print('drawn card: {}\n'.format(player.draw_card()))
