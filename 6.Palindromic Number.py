def check_palindrome(num):
    return str(num)[::]==str(num)[::-1]

user_input=int(input('Enter the number:'))

if check_palindrome(user_input):
    print(f'{user_input} is a Palindromic Number')
else:
    print(f'{user_input} is not a Palindromic number')