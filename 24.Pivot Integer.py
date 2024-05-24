def find_pivot_integer(num):
    total_sum=num*(num+1)//2
    sum=0
    if num==1:return 1
    for i in range(num):
        sum+=i
        if sum==total_sum:
            return i
        else:
            total_sum-=i
    return -1

user_range=int(input('Enter the range to find the pivot integer:'))

if find_pivot_integer(user_range)!=-1:
    print(f'In the given range of {user_range},'
          f'The pivot integer is {find_pivot_integer(user_range)}')

else:
    print('There is no pivot integer in given range')