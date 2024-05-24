'''def max_length(user_str):
    a=list(map(str,user_str.split(' ')))
    x={i:len(i) for i in a}
    max_len=max(x.values())
    for i,j in x.items():
        if j==max_len:
            print(f'"{i}" is the longest word in given string')

user_str=input('Enter a string:')
max_length(user_str)
'''

s='hello kumasr'
w=s.split(' ')
print(max(w,key=len))