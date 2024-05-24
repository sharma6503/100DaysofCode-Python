def check_armstrong(num):
    temp=num
    sum=0
    for i in str(temp):
        sum+=int(i)**len(str(temp))
    return True if sum==num else False

arr=list(map(int,input('Enter the array elements:').split(' ')))
armstrong_numbers=[]
for i in arr:
    if check_armstrong(i)==True:
        armstrong_numbers.append(i)
if not armstrong_numbers:
    print('No Armstrong Numbers in the List')
else:
    print(f'Armstrong numbers in the list ->{armstrong_numbers}')
