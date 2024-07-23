def ugly_number(number):
    while number>=1:
        if number%2==0:
            number//=2
        elif number%3==0:
            number//=3
        elif number%5==0:
            number//=5
        elif number==1:
            return True
        else:return  False

number=int(input('Enter a number:'))

if ugly_number(number):
    print(f'{number} is an ugly number')
else:
    print(f'{number} is not an ugly number')