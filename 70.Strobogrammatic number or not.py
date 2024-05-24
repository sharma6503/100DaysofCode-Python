def rotate_a_number(n):
    if n == '0':    return '0'
    elif n == '1':  return '1'
    elif n == '8':  return '8'
    elif n == '6':  return '9'
    elif n == '9':  return '6'
def check_strobogrammatic_or_not(number):
    is_strobogrammatic = True
    for i in range(len(number)):
        if number[i] != rotate_a_number(number[len(number) - i - 1]):
            is_strobogrammatic = False
    if is_strobogrammatic:
        print(f'{number} is a Strobogrammatic Number')
    else:
        print(f'{number} is not a Strobogrammatic Number')


number=input('Enter a number:')

check_strobogrammatic_or_not(number)
