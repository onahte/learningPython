# Calculate your weight from lbs to kg.

weight = input('Please enter your weight in lbs: ')
print('You weigh ' + str(int(weight)*.453) + 'kg.')

# Learned input() is str class and so numbers must be passed through int() or some
# other number class. Likewise, concattenation is only allowed for like objects.