def sum_of_ap__series(first,difference,range):

    sum=i=0
    while i<range:
        sum+=first
        first+=difference
        i+=1
    return sum

first,difference,range=map(int,input('Enter the first '
                                     'element,difference,range:').split(','))

print(f'The sum of Arithmetic series '
      f'in the given range is {sum_of_ap__series(first, difference, range)}')