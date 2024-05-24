def plus_one(digits):
    s=''
    for i in digits:
        s+=str(i)
    x=int(s)+1
    y=list(map(int,str(x)))
    return y

digits=list(map(int,input('Enter the digits:').split(' ')))

print(f'Original digits array:{digits}'
      f'\nPlus one digits array:{plus_one(digits)}')