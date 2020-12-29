#Fun little game of Rock, Paper, Scissor

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

game = [rock, paper, scissor]
computer = random.choice(game)
player = input('Rock, Paper, Scissor. Shoot!\n').lower()
outcome_choices = ['tie', 'win', 'lose']
outcome = ''

if player == 'rock':
  player = rock
  if computer == rock:
    outcome = outcome_choices[0]
  elif computer == paper:
    outcome = outcome_choices[2]
  else:
    outcome = outcome_choices[1]
elif player == 'paper':
  player = paper
  if computer == rock:
    outcome = outcome_choices[1]
  elif computer == paper:
    outcome = outcome_choices[0]
  else:
    outcome = outcome_choices[2]
else:
  player = scissor
  if computer == rock:
    outcome = outcome_choices[2]
  elif computer == paper:
    outcome = outcome_choices[1]
  else:
    outcome = outcome_choices[0]

print(f'You\n{player}')
print(f'Computer\n{computer}')
print(f"It's a {outcome}.")