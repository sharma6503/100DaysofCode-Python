def append_characters(str1,str2):
    i,j=0,0
    while i<len(str1) and j<len(str2):
        if str1[i]==str2[j]:
            j+=1
        i+=1
    return len(str2)-j



str1=input('Enter first string:').lower()
str2=input('Enter second string:').lower()

print(f'Minimum Characters to append to Make Subsequence-'
      f'{append_characters(str1,str2)}')