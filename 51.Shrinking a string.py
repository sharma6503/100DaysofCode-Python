def shrink(s):
    strs=sorted(set(s))
    ans=''
    for i in strs:
        ans+=i+str(s.count(i))
    return ans

user_str=input('Enter a String:')

print(f'Original String->{user_str}\n'
      f'Compacted String->{shrink(user_str)}')
