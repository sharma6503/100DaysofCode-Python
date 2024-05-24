def char_count(user_str):
     without_duplicate=[]
     for i in user_str.lower() :
         if i not in without_duplicate and i!=' ':
             without_duplicate.append(i)

     for i in without_duplicate:
         print(f'{i} occurs {user_str.lower().count(i)} times in {user_str}')

user_string=input('Enter a string:')

char_count(user_string)