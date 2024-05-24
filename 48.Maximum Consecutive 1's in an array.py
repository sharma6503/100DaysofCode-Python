def find_max(arr):
    current_count=max_count=0
    #To find the count of consecutive 1's
    for i in arr:
        if i==1:
            current_count+=1
        else:
            #To store the maximum count
           max_count=max(current_count,max_count)
           current_count=0
            #To whether the maximum number consecutive 1's occurs at the end of array
    return max(max_count,current_count)

arr=list(map(int,input('Enter array elements:').split()))

print(f'The Maximum Number of Consequtive 1\'s in Given array is->'
      f'{find_max(arr)}')