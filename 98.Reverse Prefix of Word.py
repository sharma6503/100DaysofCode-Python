def reverse_prefix(str,ch):

    idx=str.find(ch)+1

    return str[:idx][::-1]+str[idx:]


str=input('Enter a string:')

ch=input('Enter a character:')

print(f'Original Word->{str}\n'
      f'Prefix Reversed Word->{reverse_prefix(str,ch)}')