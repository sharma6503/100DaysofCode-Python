def is_close(str1,str2):
    if len(str1)!=len(str2):return False
    str2_without_duplicates=set(str2)
    freq_of_str1,freq_of_str2=[],[]
    for i in str2_without_duplicates:
        freq_of_str1.append(str1.count(i))
        freq_of_str2.append(str2.count(i))
    freq_of_str1.sort()
    freq_of_str2.sort()
    return freq_of_str1==freq_of_str2

str1=input('Enter the str1:')

str2=input('Enter the str2:')

if is_close(str1,str2):
    print(f'You can attain str2 from str1,so the given strings are close')
else:
    print(f'You can\'t attain str2 from str1,'
          f'so the given strings are not close')