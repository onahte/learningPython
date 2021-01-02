def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

operations = {
  '+' : add,
  '-' : subtract,
  '*' : multiply,
  '/' : divide,
}

num1 = int(input('Enter a number: '))
operations_str = ""
for key in operations:
  operations_str += key + " "
print(operations_str)
cont = 'True'
while cont:
  operation_input = input('Select an operand: ')
  num2 = int(input('Another number: '))
  answer = operations[operation_input](num1, num2)
  print(f'{num1} {operation_input} {num2} = {answer}')
  num1 = answer
  calc = input("Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
  if calc != 'y':
    cont = False