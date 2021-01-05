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
break_loop = 'False'

print('Welcome to Blackjack!')
print('The dealer deals the cards.\n')

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

def test(dealer_total, player_total):
  if dealer_total > 21:
    print('Dealer goes bust! You win!')
    break_loop = 'True'
    return break_loop
  elif dealer_total == 21:
    print('Dealer has Blackjack! You lose.')
    break_loop = 'True'
    return break_loop
  elif player_total == 21:
    print('You have BlackJack! You win!')
    break_loop = 'True'
    return break_loop
  elif player_total > 21:
    print("You've gone bust! You lose.")
    break_loop = 'True'
    return break_loop

def hit():
    cont = 'y'
    while cont == 'y':
      hit_stay = input("Would you like to stay or hit? (enter 's' or 'h'): ").lower()
      if hit_stay == 's':
        if dealer_total < player_total:
          print('You win!')
          cont = 'n'
          break_loop = 'True'
          return break_loop
        else:
          print('You lose.')
          cont = 'n'
          break_loop = 'True'
          return break_loop
      elif hit_stay == 'h':
        player_hand.append(random.choice(cards))
        print('You are dealt another card...')
        print_hand(player_hand)
        player_total = hand_value(player_hand)
        print("Your hand's total is:", player_total)
        print()
        cont = 'n'
      else:
         print("Please enter 's' or 'h'.")

player_hand = []
player_hand.append(card_random(cards))
player_hand.append(card_random(cards))
player_total = hand_value(player_hand)

dealer_hand = []
dealer_hand.append(card_random(cards))
dealer_hand.append(card_random(cards))
dealer_total = hand_value(dealer_hand)

print(f"Dealer's hand:")
print_hand(dealer_hand)
print("Dealer's total is:", dealer_total)
print('------------------')
print("Your hand:")
print_hand(player_hand)
print("Your hand's total is:", player_total)
print()

while hand_value(dealer_hand) < 21:
    while hand_value(dealer_hand) < 16:
        input('Press enter to continue...')
        print()
        dealer_hand.append(random.choice(cards))
        print('Dealer takes a hit. His new hand is: ')
        print_hand(dealer_hand)
        dealer_total = hand_value(dealer_hand)
        print("Dealer's total is:", dealer_total)
        print('------------------')
        test(dealer_total, player_total)
        if break_loop == 'True':
            break
        else:
            hit()
            test(dealer_total, player_total)
            if break_loop == 'True':
                break
    test(dealer_total, player_total)
    if break_loop == 'True':
        print('You went bust! You lose.')
        exit()
    if hand_value(player_hand) > hand_value(dealer_hand):
        if hand_value(player_hand) > 21:
            print('You went bust! You lose.')
        elif hand_value(player_hand) == 21:
            print('Blackjack! You win!')
        else:
            print('You win!')
        exit()
    else:
        hit()
if hand_value(dealer_hand) > 21:
    print('Dealer goes bust. You win!')