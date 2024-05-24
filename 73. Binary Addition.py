def add_binary(n1,n2):
    '''    sum=int(n1,2)+int(n2,2)
    s=''
    if sum==0:
        return '0'
    while sum!=0:
        s+=str(sum%2)
        sum//=2
    return s[::-1]'''



n1=input('Enter the first binary number:')

n2=input('Enter the second binary number:')

print(f'The sum of {n1,n2} is {add_binary(n1,n2)}')