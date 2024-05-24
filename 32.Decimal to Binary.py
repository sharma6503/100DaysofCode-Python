def decimal_to_binary(num):
    binary=''
    while num!=0:
        remainder=num%2
        binary+=str(remainder)
        num//=2
    return binary[::-1]

decimal_number=int(input('Enter a Decimal number:'))

print(f'Binary equivalent of {decimal_number} is'
      f' {decimal_to_binary(decimal_number)}')