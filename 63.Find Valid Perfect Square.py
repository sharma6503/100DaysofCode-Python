def valid_square(v):
   start=0
   end=v
   while(start<=end):
       m=(start+end)//2
       square=m*m
       if square==v:
           return True
       elif square>v:
           end=m-1
       else:
           start=m+1
   return -1

value=int(input('Enter a number:'))

if valid_square(value)!=-1:
    print(f'{value} is a Perfect Square')
else:
    print(f'{value} is not a Perfect Square')
