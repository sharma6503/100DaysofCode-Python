def pascal_triangle(n):
    for i in range(1,n+1):
        pascal=1
        for j in range(1,i+1):
            print(pascal,end=' ')
            pascal=pascal*(i-j)//j

        print()


n=int(input('Enter the range to print the pascal triangle:'))

print(f'\n💥💥💥Pascal Right Triangle for {n} rows💥💥💥\n')

pascal_triangle(n)


n=10
p=[]

for i in range(n):
   l=[]
   for j in range(i+1):
      if j==0 or j==i:
         l.append(1)
      else:
         x=p[i-1]
         l.append(x[j]+x[j-1])
   p.append(l)
print(p)