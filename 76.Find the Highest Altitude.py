def find_highest_altitude(gain):
    start=0
    high_altitude=0
    for i in gain:
        start+=i
        high_altitude=max(high_altitude,start)
    return high_altitude

gain=list(map(int,input('Enter the gain array:').split(' ')))

print(f'The highest altitude is ->{find_highest_altitude(gain)}')
