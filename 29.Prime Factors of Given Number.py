def prime_factors(num):
    factors=[]
    for i in range(1,num):
        is_prime = True
        if num%i==0:
            for j in range(2,i):
                if i%j==0:
                    is_prime=False
            if is_prime:
               factors.append(i)
    return factors

user_input=int(input('Enter a number:'))

print(f'Prime factors of {user_input} are {prime_factors(user_input)}')
