def product_of_array_except_self(arr):
    product=1
    zeros=0
    for i in arr:
        if i!=0:
            product*=i
        zeros+=i==0 #if i==0 zeros+=1
    if zeros>1:
        return [0]*len(arr)
    elif zeros==1:
        return [product if i==0 else 0 for i in arr]
    return [product//i for i in arr]

arr=list(map(int,input('Enter the array elements:').split(' ')))

print(f'Product array->{product_of_array_except_self(arr)}')
