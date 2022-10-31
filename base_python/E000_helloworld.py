# print hello world

def hello_world():
    print("Hello World")


def learning_python(name):
    print(name + ' is learning Python')


def multiplication_num(num):
    multipliedNumber = num * num
    return multipliedNumber, (num*num)/2


def nesting_Function(name):
    def nested_Function():
        print(name)
    return nested_Function
