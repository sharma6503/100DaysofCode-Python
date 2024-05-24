def reverse(num):
    sum=0
    while num!=0:
        remainder=num%10
        sum=sum*10+remainder
        num//=10
    return sum

user_input=int(input('Enter a number:'))

print(f'Reversed number is {reverse(user_input)}')