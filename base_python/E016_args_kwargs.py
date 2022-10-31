# make *args and **kwargs
def arkwargs(x, y):
    print(x, y)


def learning_args(*x, **y):
    print(x, y)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(*list)

pairs = [(1, 2), (3, 4)]

print(pairs, *pairs)

for pair in pairs:
    print(pair)

for pair in pairs:
    print(*pair)

dict = {'midas': 'gold', 'asmodeos': 'angel', 'giraffe': 'long neck'}

arkwargs(**{'x': 2, 'y': 6})

learning_args(4, 5, 3, 2, one=17, two=2)

learning_args(4, 5, 6, 7, 8, 9)

learning_args(eins=1, zwei=2, drei=3)
