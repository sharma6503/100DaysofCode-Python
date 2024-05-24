def find_beautiful_days(i,j,k):
    beautiful_days=0
    for i in range(i,j+1):
        num=str(i)
        avg=(abs(int(num)-int(num[::-1])))%k
        if avg==0:
            beautiful_days+=1
    return beautiful_days

i,j,k=map(int,input('Enter the range and divisor: ').split(' '))

print(f'The count of beautiful day in the range is->'
      f'{find_beautiful_days(i, j, k)}')