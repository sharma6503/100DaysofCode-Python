def find_max_guests(entry,exit):
    maximum=no_of_guests=0
    for i in range(len(entry)):
        no_of_guests+=entry[i]-exit[i]
        if no_of_guests>maximum:
            maximum=no_of_guests
    return maximum

Time_limit=int(input('Enter the time limit:'))
entry=list(map(int,input(f'Enter the number of guests entering '
                         f'the ship at every hour within the time limit of {Time_limit}hrs:').split(' ')))
exit=list(map(int,input(f'Enter the number of guests leaving '
                        f'the ship at every hour within the time limit of {Time_limit}hrs:').split(' ')))

print(f'{find_max_guests(entry,exit)}-> Maximum number of Guests '
      f'on Cruise at an instance')