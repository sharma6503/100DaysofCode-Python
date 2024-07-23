def possible_ways_to_climb(n):
    global steps
    final=0
    pre_final=1
    for i in range(n):
        steps=final+pre_final
        final=pre_final
        pre_final=steps
    return steps

no_of_steps=int(input('Enter the number of steps:'))

print(f'Possible number of ways to climb to the top is->'
      f'{possible_ways_to_climb(no_of_steps)}')
