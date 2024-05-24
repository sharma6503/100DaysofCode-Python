def swap(a,b):
    t=a
    a=b
    b=t
    return a,b
def swap_adjacent(user_str):
    i=0
    ans=''
    while i<len(user_str)-1:
            x,y=map(str,swap(user_str[i],user_str[i+1]))
            ans+=x
            ans+=y
            i+=2
    if len(user_str)%2==0:
        return ans
    else:
        ans+=user_str[-1]
        return ans

user_str=input('Enter a String:')
print(f'Before Swapping the adjacent element -"{user_str}"')
print(f'After Swapping the adjacent element -"{swap_adjacent(user_str)}"')
