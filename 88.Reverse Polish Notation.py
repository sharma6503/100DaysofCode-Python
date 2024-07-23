def operation(a,b,operator):
    if operator=='+':return a+b
    elif operator=='-':return a-b
    elif operator=='/':return a/b
    elif operator=='*':return a*b

def split_operands_and_operator(arr):
    i=0
    length=len(arr)
    operators='+-*/'
    while i<length:
        if arr[i] in operators:
            arr[i-2]=operation(int(arr[i-2]),int(arr[i-1]),arr[i])
            arr.pop(i-1)
            arr.pop(i-1)
            length-=2
            i-=2
        i+=1
    return arr[-1]

arr=list(map(str,input('Enter an expression array:').split(' ')))

print(f'Final answer after solving all expressions->'
      f'{split_operands_and_operator(arr)}')

