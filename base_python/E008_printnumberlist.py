# make a list  that prints a number, that many times, it counts how much is there in a line and in total


count = sum = line = 0
number = int(input("Number: "))

while count != number:
    count += 1
    sum += count * count
    for time in range(0, count):
        line = count * count
        print(count, end='')
    print(f" A soma da linha é {line}.")
print(f"\nA soma da pirâmide é {sum}.")
