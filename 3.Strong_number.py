def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)

def check_strong_or_not(num):
    sum=0
    for i in str(num):
        sum+=fact(int(i))
    return sum==num

user_input=int(input('Enter a number:'))

if check_strong_or_not(user_input):
    print(f'{user_input} is a Strong Number')
else:
    print(f'{user_input} is not a Strong Number')
