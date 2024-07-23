def great_string(s):
    great_chars=[]
    for i in s:
        if great_chars and abs(ord(i)-ord(great_chars[-1]))==32:
            great_chars.pop(-1)
        else:
            great_chars.append(i)
    return ''.join(great_chars)

s=input('Enter the string:')

print(f'Great string from the given string is->{great_string(s)}')
