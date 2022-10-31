# bhaskara neles


a = 1
b = 8
c = -9


def bhaskara():
    resultPlus = (-b + (b * b - 4 * a * c)**1/2) / 2 * a
    resultMinus = (-b - (b * b - 4 * a * c)**1/2) / 2 * a
    return resultPlus, resultMinus


print(bhaskara())  # why is it wrong?
