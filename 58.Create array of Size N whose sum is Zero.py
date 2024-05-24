def create_arr(N):
    arr=[]
    size=N//2
    for i in range(-size,size+1):
        arr.append(i)
    return arr

N=int(input('Enter the Size of array:'))

print(f'Array->{create_arr(N)}\n'
      f'Sum of Array->{sum(create_arr(N))}')
