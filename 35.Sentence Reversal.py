def reverse_sentence(user_str):

    return ' '.join(user_str.strip().split(' ')[::-1])



user_str=input('Enter a string:').lower()

print(f'Given Sentence "{user_str}"\n'
      f'Reversed Sentence "{reverse_sentence(user_str)}"')
