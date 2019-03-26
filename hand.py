class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.add_value(card)
        self.cards.append(card)
        self.adjust_for_ace if card.rank == "Ace" else None

    def adjust_for_ace(self):
        self.aces += 1

    def show_card(self, card=None):
        if card is None:
            card = self.cards[0]
        print(f"This card is { card }")

    def show_all_cards(self):
        for card in self.cards:
            print(f"Card is { card }")
        print(f"The value is: {self.value}")

    def add_value(self, card):
        if card.rank == 'Ace' and self.value + 11 > 21:
            self.value += 1
        else:
            self.value += card.value
