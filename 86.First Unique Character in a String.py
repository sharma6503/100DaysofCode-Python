def find_first_unique_char(s):
    s_without_duplicates=''
    for i in s:
        if i not in s_without_duplicates:
            s_without_duplicates+=i
    for i in s_without_duplicates:
        if s.count(i)==1:
            return s.index(i)
    return -1

s=input('Enter a string:').lower()

if find_first_unique_char(s)!=-1:
    print(f'First unique character occurs in index->{find_first_unique_char(s)}')
else:
    print('No unique characters present in the string')