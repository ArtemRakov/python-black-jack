class Interface:
    def take_bet(self, chips):
        bet = int(input('What is your bet?'))
        self.check_if_can_bet(bet, chips)
        chips.bet = bet
        return bet

    def check_if_can_bet(self, bet, chips):
        if bet > chips.total:
            print('Cant bet')
            self.take_bet(chips)

    def burst(self, hand):
        if hand.value > 21:
            return True

    def show_hands(self, player_hand, dealer_hand):
        print('Diller hand:')
        dealer_hand.show_card()
        print('Player hand:')
        player_hand.show_all_cards()

    def show_hands_end(self, player_hand, dealer_hand):
        print('Diller hand:')
        dealer_hand.show_all_cards()
        print('Player hand:')
        player_hand.show_all_cards()

    def dealer_take_cards(self, dealer_hand, cards):
        while dealer_hand.value < 17:
            dealer_hand.add_card(cards.deck.pop())

    def result(self, player_hand, dealer_hand, chips):
        if player_hand.value > 21:
            self.player_busts()
            chips.lose_bet()
        elif dealer_hand.value > 21:
            self.dealer_busts()
            chips.win_bet()
        elif player_hand.value > dealer_hand.value:
            self.player_wins()
            chips.win_bet()
        elif dealer_hand.value > player_hand.value:
            self.dealer_wins()
            chips.lose_bet()
        else:
            self.push()

    def players_take_cards(self, player_hand, dealer_hand, cards):
        for _ in range(2):
            player_hand.add_card(cards.deck.pop())
            dealer_hand.add_card(cards.deck.pop())

    def player_busts(self):
        print("Player bust number exceed 21")

    def player_wins(self):
        print("Player won")

    def dealer_busts(self):
        print("Dealer busts")

    def dealer_wins(self):
        print("Dealer won")

    def push(self):
        print("Draw")

    def balance(self, chips):
        print(f'Balance: {chips.total}')

    def new_game(self):
        answer = input('More?')
        return answer == 'y' or answer == 'yes'

    def hit_or_pass(self, player_hand, cards):
        global playing
        answer = input("Hit or pass?")
        if answer == 'hit':
            player_hand.add_card(cards.deck.pop())
            player_hand.show_all_cards()
            return True
        else:
            return False
