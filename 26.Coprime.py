def coprime(num1,num2):
    hcf=0
    for i in range(1,min(num1,num2)+1):
        if num1%i==0 and num2%i==0:
            hcf=i
    if hcf==1: return True
    else:return False


num1=int(input('Enter the first number:'))

num2=int(input('Enter the second number:'))

if coprime(num1,num2):
    print(f'{num1,num2} are coprime numbers')

else:
    print(f'{num1,num2} are not coprime numbers')