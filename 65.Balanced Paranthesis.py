def check_balanced(paranthesis):
    stack=[]
    for i in paranthesis:
        if i=='{':
           stack.append('}')
        elif i=='[':
            stack.append(']')
        elif i=='(':
            stack.append(')')
        elif not stack or stack.pop()!=i:
            return False
    return True if not stack else False

paranthesis=input('Enter the Paranthesis:')

if check_balanced(paranthesis)==True:
    print(f'"{paranthesis}" is a Balanced Paranthesis')
else: print(f'"{paranthesis}" is not a Balanced Paranthesis')
