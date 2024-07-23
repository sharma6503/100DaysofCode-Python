def find_frequent_number_after_key(arr,key):
    global ans
    frequent_numbers=[arr[i+1] for i in range(len(arr)-1) if arr[i]==key]
    frequent_numbers_without_duplicates=set(frequent_numbers)
    count=0
    for i in frequent_numbers_without_duplicates:
        a=frequent_numbers.count(i)
        if a>count:
            count=a
            ans=i
    return ans

arr=list(map(int,input('Enter array elements:').split(' ')))
key=int(input('Enter the key values:'))

print(f'The Most Frequent Character after the Key Value is->'
      f'{find_frequent_number_after_key(arr,key)}')