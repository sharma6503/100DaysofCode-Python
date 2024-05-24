def find_even_no_of_digit_elements(arr):
    count=0
    for i in arr:
        length=len(str(i))%2
        if length==0:
            count+=1
    return count


arr=list(map(int,input('Enter the array elements:').split(' ')))

print(f'Elements with Even No.of Digits in the given array is->'
      f'{find_even_no_of_digit_elements(arr)}')