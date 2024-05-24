'''def check_power(number):
    while number>1:
        if number%4!=0:return False
        number/=4
    return True if number==1 else False

number=int(input('Enter a number:'))

if check_power(number):
    print(f'{number} is power of 4')
else:
    print(f'{number} is not a power of 4')
'''
N= int(input("Enter the number: "))
flag = 1
num=N
while num > 1:
    if num % 4 != 0:
        flag = 0
    num /=4
if num == 1:
         flag = 1
else:
         flag = 0
if flag == 1:
    print(f'{N} is a power of 4')
else:
    print(f'{N} is not a power of 4')