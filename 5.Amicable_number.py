def factor_sum(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    return sum

def check_amicable(num1,num2):
    return  num1==factor_sum(num2) and num2==factor_sum(num1)

user_input1=int(input('Enter the value of num1:'))
user_input2=int(input('Enter the value of num2:'))

if check_amicable(user_input1,user_input2):
    print(f'{user_input1,user_input2} are Amicable numbers')
else:
    print(f'{user_input1, user_input2} are not Amicable numbers')