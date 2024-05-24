def gcd(num1,num2):
   while num2:
       num1,num2=num1,num1%num2
       return num1


num1=int(input('Enter the first number:'))
num2=int(input('Enter the second number:'))

print(f'GCD of Two numbers is {gcd(num1, num2)}')
