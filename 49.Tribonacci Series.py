def tribonacci(num):
    if num==0:return 0
    elif  num==1 or num==2:return 1
    else: return tribonacci(num-1)+tribonacci(num-2)+tribonacci(num-3)


def tribonacci_series(num):
    print('💥💥Tribonacci Series💥💥')
    for i in range(num):
        series=tribonacci(i)
        print(series,end=' ')

num=int(input('Enter the range of tribonacci series:'))

tribonacci_series(num)

