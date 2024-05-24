def second_maximum(user_list):
    first_max=0
    second_max=0
    for i in user_list:
        if i>first_max:
            second_max = first_max
            first_max=i

        if i<first_max and second_max<i:
            second_max=i

    return second_max

user_list=list(map(int,input('Enter elements in the list separated by a space:').split(' ')))

ans=second_maximum(user_list)

print(f'{ans} is the Second Maximum Element in the List')