x = [[x for x in range(5)] for x in range(6)]

i = {i for i in range(100) if i % 9 == 0 or i % 7 == 0}

print(x, '\n', i)
