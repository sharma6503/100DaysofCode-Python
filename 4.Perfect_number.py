def check_perfect(num):
    sum=0
    for i in range (1,num):
        if num%i==0:
            sum+=i
    return sum==num

user_input=int(input('Enter a number:'))

if check_perfect(user_input):
    print(f'{user_input} is a Perfect number')
else:print(f'{user_input} is not a Perfect number')