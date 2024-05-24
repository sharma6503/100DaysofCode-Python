def check_armstrong(num):
    sum=0
    power=len(str(num))
    for i in str(num):
        sum+=int(i)**power
    return sum==num

user_input=int(input('Enter a number:'))

if check_armstrong(user_input):
    print(f'{user_input} is an Armstrong')
else:
    print(f'{user_input} is not an Armstrong')