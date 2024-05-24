def compare_version(v1,v2):
    level1=v1.split('.')
    level2=v2.split('.')
    length=max(len(level1),len(level2))

    for i in range(length):
        position1=int(level1[i]) if i<len(level1) else 0
        position2=int(level2[i]) if i<len(level2) else 0

        if position1<position2:
            return False
    return True

v1=input('Enter the First Version:')
v2=input('Enter the Second Version:')

if compare_version(v1,v2):
    print(f'{v1} is greater version than {v2}')
else:
    print(f'{v2} is greater vesion than {v1}')