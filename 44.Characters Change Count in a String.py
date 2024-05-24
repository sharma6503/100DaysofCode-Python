def count_char_change(user_str):
    change_count=0
    for i in range(len(user_str)):
        if i<len(user_str)-1 and user_str[i]!=user_str[i+1]:
            change_count+=1
    return change_count

user_string=input('Enter a String:').lower()

print(f'Number of character changes in given string {user_string}->'
      f'{count_char_change(user_string)}')