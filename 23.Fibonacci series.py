def fibo_series(num):
    if num ==0:return 0
    elif num==1:return 1
    else: return  fibo_series(num-1)+fibo_series(num-2)

def fibo_series_range(fibo_range):
    for num in range(fibo_range):
        print(fibo_series(num),end=' ')

fibo_range=int(input('Enter the range for fibonacci series to be printed:'))

fibo_series_range(fibo_range)