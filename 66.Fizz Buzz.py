def fizz_buzz(num):
    fizz_buzz_arr=[]
    for i in range(1,num+1):
        if i%3==0 and i%5==0:
            fizz_buzz_arr.append('Fizz Buzz')
        elif i%5==0:
            fizz_buzz_arr.append('Buzz')
        elif i%3==0:
            fizz_buzz_arr.append('Fizz')
        else:
            fizz_buzz_arr.append(str(i))
    return fizz_buzz_arr

N=int(input('Enter the array range:'))

print(f'💥💥Fizz Buzz Array💥💥\n'
      f'{fizz_buzz(N)}')