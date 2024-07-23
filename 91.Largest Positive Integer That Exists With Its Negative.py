def find_largest_number(arr):
    max_number=-1
    for i in arr:
        if -i in arr:
            max_number=max(i,max_number)
    return max_number

arr=list(map(int,input('Enter array elements:').split(' ')))

print(f'Largest positive integer that  exists with '
      f'its negative is->{find_largest_number(arr)}')
