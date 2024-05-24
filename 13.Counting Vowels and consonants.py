def count(user_str):
    vowels=0
    consonants=0
    for i in user_str:
        if i in 'aeiou':
            vowels+=1
        elif i.isalpha() and i not in 'aeiou':
            consonants+=1
    print(f'"{user_str}" consists {vowels} vowels and {consonants} consonants')

user_str=input('Enter a string:')

count(user_str)