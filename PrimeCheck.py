def prime_checker(number):
    prime_check = 'True'
    for x in range(2, number + 1):
        if number % x == 0:
            if x != number:
                prime_check = 'False'
    if prime_check == 'False':
        print('not prime')
    else:
        print('prime')

n = int(input("Check this number: "))
prime_checker(number=n)