def insert_element(arr,target):

    start,end=0,len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            end = mid - 1
        else:
            start=mid+1
    return start

arr=list(map(int,input('Enter array elements:').split(' ')))

target=int(input('Enter a Target Value:'))

print(f'{target} can be inserted at the index of {insert_element(arr,target)} '
      f'to maintain the flow of sorted array ')



