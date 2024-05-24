def check_alike_or_not(s):
    a=s[:len(s)//2]
    b=s[len(s)//2:]
    c1,c2=0,0
    for i in range(len(s)//2):
        if a[i] in 'AEIOUaeiou':
            c1+=1
        if b[i] in 'AEIOUaeiou':
            c2+=1
    return c1==c2

s=input('Enter a String:')

if check_alike_or_not(s):
    print(f'The Given String Halves are Alike')
else:
    print(f'The Given String Halves are not Alike')