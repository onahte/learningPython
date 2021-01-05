import random
from sys import exit

cards_list = [
  ['Diamonds',2],
  ['Diamonds',3],
  ['Diamonds',4],
  ['Diamonds',5],
  ['Diamonds',6],
  ['Diamonds',7],
  ['Diamonds',8],
  ['Diamonds',9],
  ['Diamonds',10],
  ['Diamonds','Jack'],
  ['Diamonds','Queen'],
  ['Diamonds','King'],
  ['Diamonds','Ace'],
  ['Hearts',2],
  ['Hearts',3],
  ['Hearts',4],
  ['Hearts',5],
  ['Hearts',6],
  ['Hearts',7],
  ['Hearts',8],
  ['Hearts',9],
  ['Hearts',10],
  ['Hearts','Jack'],
  ['Hearts','Queen'],
  ['Hearts','King'],
  ['Hearts','Ace'],
  ['Clovers',2],
  ['Clovers',3],
  ['Clovers',4],
  ['Clovers',5],
  ['Clovers',6],
  ['Clovers',7],
  ['Clovers',8],
  ['Clovers',9],
  ['Clovers',10],
  ['Clovers','Jack'],
  ['Clovers','Queen'],
  ['Clovers','King'],
  ['Clovers','Ace'],
  ['Spades',2],
  ['Spades',3],
  ['Spades',4],
  ['Spades',5],
  ['Spades',6],
  ['Spades',7],
  ['Spades',8],
  ['Spades',9],
  ['Spades',10],
  ['Spades','Jack'],
  ['Spades','Queen'],
  ['Spades','King'],
  ['Spades', 'Ace'],
  ]
cards = cards_list

def card_random(cards):
  random_card = random.choice(cards)
  card = random_card
  cards.remove(card)
  return random_card

def card_value(card):
  if card[1] == 'Jack':
    return 10
  elif card[1] == 'Queen':
    return 10
  elif card[1] == 'King':
    return 10
  elif card[1] == 'Ace':
    return 1
  else:
    return card[1]

def hand_value(hand):
  total = 0
  for card in hand:
    total += card_value(card)
    if card[1] == 'Ace':
      if total < 12:
        total += 10
  return total

def print_hand(hand):
  for card in hand:
    print(f'{card[1]} of {card[0]}')

def compare(dealer_total, player_total):
    if player_total > dealer_total:
        return 'You win!'
    elif dealer_total > player_total:
        return 'You lose.'
    else:
        return "It's a draw."

def hit(player_hand):
    cont = 'True'
    while cont == 'True':
        hit_stay = input("Would you like to stay or hit? (enter 's' or 'h'): ").lower()
        if hit_stay == 's':
            cont = 'False'
            return player_hand
        elif hit_stay == 'h':
            print('You are dealt another card...')
            player_hand.append(random.choice(cards))
            print_hand(player_hand)
            player_total = hand_value(player_hand)
            print("Your hand's total is:", player_total)
            print()
            if player_total >= 21:
                cont = 'False'
                return player_hand
        else:
            print("Please enter 's' or 'h'.")

def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

game = (input("Do you want to play a hand of Blackjack? ('y' or 'n') ")).lower()
if game == 'y':
    game_play = 'True'
else:
    game_play = 'False'

while game_play:
    break_dealer = 'True'
    game_play = 'False'

    print(logo)
    print('Welcome to Blackjack!')
    print('******************************')
    print('The dealer deals the cards.\n')
    sleep(1)

    player_hand = []
    player_hand.append(card_random(cards))
    player_hand.append(card_random(cards))
    player_total = hand_value(player_hand)

    dealer_hand = []
    dealer_hand.append(card_random(cards))

    print(f"Dealer's hand:")
    print_hand(dealer_hand)
    print('Hidden')
    dealer_hand.append(card_random(cards))
    dealer_total = hand_value(dealer_hand)
    print('------------------')
    print("Your hand:")
    print_hand(player_hand)
    print("Your hand's total is:", player_total)
    print()

    if player_total < 21:
        player_hand = hit(player_hand)
        player_total = hand_value(player_hand)
    if player_total == 21:
        print('You have Blackjack!')
        print()
    elif player_total > 21:
        print('You have gone bust! You lose.')
        print()
        break_dealer = 'False'
    print('The dealer shows his cards:')
    print_hand(dealer_hand)
    print("Dealer's total is:", dealer_total)
    print()
    while break_dealer == 'True' and dealer_total < 17:
        input('Press enter to have the dealer deal himself another card...')
        print()
        dealer_hand.append(random.choice(cards))
        print('Dealer takes a hit. His new hand is: ')
        print_hand(dealer_hand)
        dealer_total = hand_value(dealer_hand)
        print("Dealer's total is:", dealer_total)
        print('------------------')
    if dealer_total == 21:
        print('Dealer has Blackjack!')
        print()
        break_dealer = 'False'
    elif dealer_total > 21:
        print('Dealer has gone bust! You win!')
        break_dealer = 'False'
    if dealer_total < 22 and player_total < 22:
        print(compare(dealer_total, player_total))
        print()
    sleep(1)
    print('------------------')
    game = input("Shall we play again? ('y' or 'n') ")
    if game == 'y':
        game_play == 'True'
    clear_screen()
