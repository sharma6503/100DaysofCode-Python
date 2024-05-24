def find_maximum_subarray(arr):
    sum=0
    maximum_sum=arr[0]
    for i in arr:
        sum+=i
        maximum_sum=max(sum,maximum_sum)
        if sum<0:
            sum=0
    return maximum_sum


arr=list(map(int,input('Enter the array elements:').split(' ')))

print(f'The Maximum sum of subarray of a given array is->'
      f'{find_maximum_subarray(arr)}')
