def check_palindrome(user_str):

    return user_str[::]==user_str[::-1]

user_input=input('Enter a String:')

if check_palindrome(user_input.lower()):
    print(f'{user_input} is Palindromic String')
else:
    print(f'{user_input} is not a Palindromic String')
