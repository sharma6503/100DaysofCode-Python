def find_longest_consecutive_seq(arr):
    without_duplicates_arr=list(set(arr))
    max_count= 0
    # To find the starting point
    for i in range(len(without_duplicates_arr)):
        if without_duplicates_arr[i]-1 not in without_duplicates_arr:
            count=1
            starting_point=without_duplicates_arr[i]
            #To find the count maximum count
            while starting_point+1 in without_duplicates_arr:
                count+=1
                starting_point+=1

            if count>max_count:
               max_count=count

    return max_count

arr=list(map(int,input('Enter array elements:').split(' ')))

print(f'The longest consecutive Sequence count for the given array is'
      f' ->{find_longest_consecutive_seq(arr)}')

