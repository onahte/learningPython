def prime_checker(number):
    prime_check = 'True'
    for x in range(2, number):
        if number % x == 0:
            prime_check = 'False'
    if prime_check:
        print('This number is prime.')
    else:
        print('This number is not prime.')

n = int(input("Check this number: "))
prime_checker(number=n)
