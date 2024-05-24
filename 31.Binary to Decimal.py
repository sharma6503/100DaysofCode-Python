def binary_decimal(num):
    mul=1
    decimal_value=0
    for i in range(len(num)-1,-1,-1):
        decimal_value+=int(num[i])*mul
        mul*=2
        print(i)
    return decimal_value

binary=input('Enter a Binary Number:')

print(f'The Decimal Value of {binary} is equal to {binary_decimal(binary)}')