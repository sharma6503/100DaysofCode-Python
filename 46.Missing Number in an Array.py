#To find the Missing element in the given range
#Approach:-
#1.Find the sum of all elements in the Given range using n(n+1)//2
#2.Find the sum of all array elements
#3.Subtract sum of all elements with sum of array elements

def find_missing_number(arr,range):

    return range*(range+1)//2-sum(arr)


range=int(input('Enter the range:'))
arr=list(map(int,input('Enter array elements:').split(' ')))

print(f'{find_missing_number(arr,range)} is the missing element '
      f'in given range of array')

