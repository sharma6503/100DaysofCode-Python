def deletion(user_str,delete_str):
    user_str=user_str.split()
    for i in user_str:
        if i==delete_str:
            user_str.remove(i)
    return ' '.join(user_str)





user_str=input('Enter a string:').split()

delete_str=input('Enter a string to be deleted:')

print(deletion(user_str,delete_str))



