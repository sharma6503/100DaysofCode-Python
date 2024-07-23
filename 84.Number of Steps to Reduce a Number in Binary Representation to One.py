def reduce_binary_number_to_one(binary):
    c1,c2=0,0
    decimal_equivalent=int(binary,2)
    while decimal_equivalent!=1:
        if decimal_equivalent%2==1:
            decimal_equivalent+=1
            c1+=1
        c2+=1
        decimal_equivalent//=2
    return c1+c2

binary=input('Enter a Binary Number:')

print(f'{reduce_binary_number_to_one(binary)}->'
      f'Number of steps is required to reduce the given binary representation to one')
