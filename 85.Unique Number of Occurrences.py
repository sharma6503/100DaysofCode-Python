def unique_occurence_or_not(arr):
    count_arr = [arr.count(i) for i in list(set(arr))]
    count_arr_without_duplicates = set(count_arr)
    for i in count_arr_without_duplicates:
        if count_arr.count(i) > 1:
            return False
    return True


arr = list(map(int, input('Enter array elements:').split(' ')))

print(unique_occurence_or_not(arr))