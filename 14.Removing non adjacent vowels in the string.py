'''def remove_vowels(user):
    l=list(map(str,user))
    i=0
    while i<len(l):
        if l[-1] in 'aeiou' and l[-2] not in 'aeiou': l.pop(-1)

        if i<len(l)-1 and l[i] in 'aeiou' and l[i+1] in 'aeiou':
            i+=2
        if i<len(l)-1 and l[i] in  'aeiou' and l[i+1] not in 'aeiou':
            l.pop(i)
        i+=1
    return ''.join(l)

user_input=input('Enter a string:')

print(remove_vowels(user_input))
'''

s='canteen'
a=''
for i in s:
    if i in 'aeiou':
        if s.index(i)+1==i:
            a+=i
        else:continue
    else:a+=i
print(a)