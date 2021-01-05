import random

print("""" ____ ____ ____ ____ ____ ____ 
||N |||u |||m |||b |||e |||r ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
 ____ ____ ____ ____ ____      
||G |||u |||e |||s |||s ||     
||__|||__|||__|||__|||__||     
|/__\|/__\|/__\|/__\|/__\|     """)
print('_________________________')
print('Guess a number between 1 and 10.')
print('_________________________')
print('Select difficulty level. Easy or Hard:')
level = input("Type 'e' or 'd': ")
tries = 0
if level == 'e':
  tries = 10
elif level == 'd':
  tries = 5

print()
print("Let's begin!")
rand_int = random.randint(1, 10)

def test(guess, rand_int):
  if guess > rand_int:
    return 'Too high.'
  else:
    return 'Too low.'

cont = 'True'
while cont == 'True' and tries > 0:
  guess = int(input('Make a guess: '))
  if guess == rand_int:
    print('You got it!')
    cont = 'False'
  else:
    print("Nope. That's not it.")
    print(test(guess, rand_int))
    tries -= 1
    if tries == 0:
      print(f'The number was {rand_int}.')
      print('Sorry. You lose.')
    else:
      print(f'You have {tries} guesses left.')