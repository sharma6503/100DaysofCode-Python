def str_replace(user_str,str_to_be_replace,new_str):
    return user_str.replace(str_to_be_replace,new_str)

user_str=input('Enter a string:')

str_to_be_replace=input('Enter a string to be replaced:')

new_str=input('Enter new string:')

print(str_replace(user_str,str_to_be_replace,new_str))
