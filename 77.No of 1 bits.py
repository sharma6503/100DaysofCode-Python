def find_1_bits(num):
    binary=bin(num)[2:]
    ones_count=0
    for i in binary:
        if i=='1':
            ones_count+=1
    return ones_count

num=int(input('Enter a number:'))

print(f'Number of 1\'s bits present in a given number is ->{find_1_bits(num)}')