# lists , tuples and libraries challenges

choice = 0

while choice != 3:
    choice = int(
        input("[0] Lists\n[1] Tuples\n[2] Dictionaries\n[3] Get me out!\nYour answer to the loop: "))
    if choice == 0:
        names = ["vel'Koz", "Viktor", "eduardo", "Yasuo"]
        print(names)

        names[2] = "joao"
        print(names[0:2])

        numbers = [1, 2, 3, 4, 5]
        numbers.append(6)
        print(numbers)

        numbers.insert(0, 0)
        print(numbers)
    elif choice == 1:
        names = ("Volibear", "Magronion",
                 "Erik 'the Conqueror' Vargas", "alberto")
        print(names)
    elif choice == 2:
        names = {
            'Edu': "Eduardo", 'Magros': "Mao the Gronion", 'Eic': "Erick the Dictionary example"
        }
        print(names["Edu"])
print("You were already free..")
