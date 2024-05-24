def fact(num):
    if num<=1:
        return 1
    else:
        return num*fact(num-1)

user_input=int(input('Enter a Number:'))

print(f'{user_input}! is {fact(user_input)}')