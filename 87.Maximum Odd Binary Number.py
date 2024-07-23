def find_max_odd_binary(binary):
    ones_count=binary.count('1')
    str_arr=['0']*len(binary)
    str_arr[-1]='1'
    ones_count-=1
    i=0
    while ones_count>0:
        str_arr[i]='1'
        i+=1
        ones_count-=1
    return ''.join(str_arr)


binary =input('Enter a Binary Number:')

print(f'Maximum Odd Binary Number is->"{find_max_odd_binary(binary)}"')