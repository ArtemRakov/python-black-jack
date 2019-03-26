from deck import Deck
from chips import Chips
from hand import Hand
from interface import Interface


playing = True
interface = Interface()
chips = Chips()


while True:
    playing = True
    cards = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    bet = 0
    chips.bet = interface.take_bet(chips)

    interface.players_take_cards(player_hand, dealer_hand, cards)

    interface.show_hands(player_hand, dealer_hand)

    while playing:
        if interface.burst(player_hand):
            break
        else:
            playing = interface.hit_or_pass(player_hand, cards)

    interface.dealer_take_cards(dealer_hand, cards)
    interface.show_hands_end(player_hand, dealer_hand)
    interface.result(player_hand, dealer_hand, chips)
    interface.balance(chips)

    if not interface.new_game():
        break
