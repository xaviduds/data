# Easy for: print all possible combinations of words in two lists
firstNames = ['Eduardo', 'Pedro', 'Erik', 'Antonio']
lastNames = ['the Wise', 'Wintermacher',
             'the Conqueror', 'Van der Sonne']

for firstName in firstNames:
    for lastName in lastNames:
        print(firstName, lastName)

print(f'\nYep, {firstNames[1]} {lastNames[2]} is definitely the coolest')
