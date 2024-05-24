def sum_of_pair(arr,target):
    for i in range(len(arr)):
        if i<len(arr)-1 and arr[i]+arr[i+1]==target:
            return [i,i+1]
    return -1

arr=list(map(int,input('Enter the array elements:').split(' ')))
target=int(input('Enter the target value:'))

if sum_of_pair(arr, target)!=-1:
        print(f'By adding the elements in the indices {sum_of_pair(arr, target)},'
              f'The target value of {target} is obtained')
else:
    print(f'Given array does not contains the pair of elements,'
          f'which sum is equal to the target value')