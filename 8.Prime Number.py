def check_prime(num):
    is_prime=True
    for i in range(2,num//2):
        if num%i==0:
          return False
    return is_prime

user_input=int(input('Enter a number:'))

if check_prime(user_input):
    print(f'{user_input} is a Prime number')
else:
    print(f'{user_input} is not a Prime number')
