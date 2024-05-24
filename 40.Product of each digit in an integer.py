def find_product(number):
    product=1
    while number:
        remainder=number%10
        product*=remainder
        number//=10
    return product

number=int(input('Enter an integer:'))

print(f'The Product of each digits of a given integer '
      f'{number} is {find_product(number)}')