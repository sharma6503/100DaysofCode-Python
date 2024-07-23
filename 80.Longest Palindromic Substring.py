def find_longest_palindromic_substring(s):
    palindromic_substrings=[]
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            sub_string=s[i:j]
            if sub_string==sub_string[::-1]:
                palindromic_substrings.append(sub_string)
    palindromic_substrings.sort(key=len)
    return palindromic_substrings[-1]

s=input('Enter a String:')

print(f'Longest palindromic substring is->'
      f'{find_longest_palindromic_substring(s)}')

