def roman_to_number(roman):
    if roman=='I':return 1
    elif roman=='V':return 5
    elif roman=='X': return 10
    elif roman=='L':return 50
    elif roman=='C':return 100
    elif roman=='D':return 500
    else:return 1000

def conversion(roman): #XIV
    previous=result=0
    for i in range(len(roman)-1,-1,-1): # V,I,X
        current=roman_to_number(roman[i])   #5,1,10
        if current<previous:    #5<0,1<5,10<5
            result-=current #4
        else:
            result+=current #5,14
        previous=current #5,1,10
    return result #14

roman=input('Enter a Roman Value:')

print(f'{roman} is Equal to {conversion(roman)}')