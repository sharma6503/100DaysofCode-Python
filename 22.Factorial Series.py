def fact(num):
    if num<=1:
        return 1
    else : return num*fact(num-1)

def series(factorial_range):
    for i in range(factorial_range+1):
        factorials=fact(i)
        print(f'{i}!={factorials}',end='   ')

factorial_range=int(input('Enter the range of factorial to be Printed:'))

series(factorial_range)