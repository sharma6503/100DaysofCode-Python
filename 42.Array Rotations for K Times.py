def rotate_array(arr,K):

    return (arr[K-1::-1]+arr[len(arr)-1:K-1:-1])[::-1]


arr=list(map(int,input('Enter the array elements:').split(' ')))

rotations=int(input('Enter the number of rotations to be Performed:'))

print(f'Original Array->{arr}\n'
      f'Rotated Array->{rotate_array(arr,rotations%len(arr))}')