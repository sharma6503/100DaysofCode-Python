def find_odd_even(num):
    if num&1==1:
        return False
    else:
        return True


num=int(input('Enter a Number:'))

if find_odd_even(num):
    print(f'{num} is an even number')
else:
    print(f'{num} is an odd number')