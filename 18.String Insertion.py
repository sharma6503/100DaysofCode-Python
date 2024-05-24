def insertion(user_str,insert,idx):
    return user_str[:idx]+insert+user_str[idx:]



user_str=input('Enter a string:')
idx=int(input('Enter the position to insert sub string:'))
sub_string=input('Enter a sub string to be inserted:')

print(insertion(user_str,sub_string,idx))