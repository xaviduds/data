x = 5


def local(name):
    x = name
    return x


print(local('carlitos'))

'''
global_test = 'mario'


def globaltest(name):
    global global_test
    global_test = name
    return global_test


print(global_test('carlitos'))
'''
