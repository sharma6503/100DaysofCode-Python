def find_max_subarray_sum(arr,k):
    max_sum=0
    window_sum=sum(arr[:k])
    max_sum=max(max_sum,window_sum)
    for i in range(k,len(arr)):
        window_sum=window_sum-arr[i-k]+arr[i]
        max_sum=max(max_sum,window_sum)

    return max_sum

arr=list(map(int,input('Enter array elements:').split(' ')))

k=int(input('Enter the size of window:'))

print(f'Maximum Subarray Sum of Size K->'
      f'{find_max_subarray_sum(arr,k)}')