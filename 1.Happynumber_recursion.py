def loop(a):
	sum=0
	for i in str(a):
		sum+=int(i)**2
	return sum

def check(ans):
    if ans == 1 or ans==7: return True
    elif ans<10: return False
    else: return check(loop(ans))


a=43636455
ans=loop(a)
if check(ans)==True:
    print(f'{a} is a Happy Number')
else:
    print(f'{a} is not a Happy Number')

