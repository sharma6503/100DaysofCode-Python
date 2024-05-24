def check_anagram(user1,user2):
    return sorted(user1)==sorted(user2)

user_str1=input('Enter your first string:')
user_str2=input('Enter your second string:')

if check_anagram(user_str1.lower(),user_str2.lower()):
    print(f'{user_str1} and {user_str2} are Anagram Strings')
else:
    print(f'{user_str1} and {user_str2} are not an Anagram Strings')