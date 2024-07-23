def reverse_vowels(s):

    s_list=[i for i in s]
    reversed_vowels=[i for i in s if i in 'aeiouAEIOU'][::-1]
    idx=0
    for i in range(len(s_list)):
        if s_list[i] in 'aeiouAEIOU':
            s_list[i]=reversed_vowels[idx]
            idx+=1
    return ''.join(s_list)

s=input('Enter a string:')

print(f'Actual String->{s}'
      f'\nVowels Reversed String->{reverse_vowels(s)}')