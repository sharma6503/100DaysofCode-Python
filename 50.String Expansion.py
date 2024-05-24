def expand_string(s):
    char=num=ans=''
    for i in s:
        if i.isnumeric():
            num+=i
        else:
            if num=='' and char!='':
                ans+=char
            elif num !='' and char!='':
                ans+=char*int(num)
            char=i
            num=''
    if num !='' and char!='':
                ans+=char*int(num)
    return  ans

s=input('Enter the String:').lower()

print(f'Original String->{s}\n'
      f'Expanded String->{expand_string(s)}')

