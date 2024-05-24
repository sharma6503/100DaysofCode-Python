def find_minimum_common_integer(arr1,arr2):
    common_integers=set(arr1).intersection(set(arr2))
    if not common_integers:
        return -1
    else:
        return min(common_integers )


arr1=list(map(int,input('Enter the first array elements:').split(' ')))

arr2=list(map(int,input('Enter the second array elements:').split(' ')))

if find_minimum_common_integer(arr1,arr2)!=-1:
    print(f'The minimum common integer in both array is->'
          f'{find_minimum_common_integer(arr1, arr2)}')
else:
    print('There is no common integer in both arrays')