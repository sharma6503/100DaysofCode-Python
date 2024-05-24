def sum_of_GP_series(first,common_ratio,range):
    i=0
    sum=0
    while i<range:
        sum+=first
        first*=common_ratio
        i+=1
    return sum

first,common_ratio,range=map(int,input('Enter the '
                                       'first element,common ratio,range:').split(','))

print(f'The sum of GP series for the given input is '
      f'{sum_of_GP_series(first, common_ratio, range)}')