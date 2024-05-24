def is_subsequence(str1,str2):
    i,j=0,0
    while j<len(str2):
        if str1[i]==str2[j]:
            i+=1
        if i==len(str1):
            return True
        j+=1
    return False

str1=input('Enter first string:')
str2=input('Enter second string:')

if is_subsequence(str1,str2):
    print(f'"{str1} "is a subsequence of "{str2}"')
else:
    print(f'"{str1} "is not a subsequence of "{str2}"')
