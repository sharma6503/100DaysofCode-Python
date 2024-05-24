def sum_of_cubes(M,N):
    sum=0
    if M>=N:return 0
    else:
        for i in range(M,N+1):
            sum+=i**3
    return sum


M,N=map(int,input('Enter the values of M and N:').split(' '))

if sum_of_cubes(M, N):
    print(f'Sum of cubes of values inclusive of the range {M,N} is->'
          f'{sum_of_cubes(M,N)}')
else:
    print(f'Range is exclusively')