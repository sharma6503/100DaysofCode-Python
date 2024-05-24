def covert_to_roman(num):

    values=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    roman_letters=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    roman_value=''
    for i in range(len(values)):
        while num>=values[i]:
            num=num-values[i]
            roman_value+=roman_letters[i]
    return roman_value


user_input=int(input('Enter a number:'))

print(f'{user_input} is Equal to {covert_to_roman(user_input)}')



