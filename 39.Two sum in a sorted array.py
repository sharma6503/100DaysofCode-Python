def two_sum(arr,target):
    left=0
    right=len(arr)-1
    while left<right:
        sum=arr[left]+arr[right]
        if sum==target:
            return [left,right]
        elif sum>target:
            right-=1
        else:
            left+=1

arr=list(map(int,input('Enter the array elements in ascending order:').split(' ')))

target=int(input('Enter the target value:'))

print(f'{target} can be obtained by adding '
      f'the values present in the indices {two_sum(arr, target)}')