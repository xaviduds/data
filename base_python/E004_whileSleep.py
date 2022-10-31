# make an easy and a complicated while loop
from time import sleep


number, count = 3, 0

if number > 5:
    print(f"{number} is bigger than 5, no addition necessary.")
elif number == 5:
    print("It's already five.")
else:
    while number < 5:
        number += 1
        count += 1
    print("Calculating.", end="")
    sleep(1)
    print('.', end="")
    sleep(1)
    print('.', end="")
    sleep(3)
    print(' (O_O;) "Is that right?"')
    sleep(4)
    print('Double checking...', end="")
    sleep(4)
    print(' Yeah probably')
    sleep(2)
    print(f"Your number definitely took {count} additions to become 5.")
