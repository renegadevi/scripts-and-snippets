# Examples of python alternatives of 'switch-case'


# 1: get a dict value
dict = {'a': 1, 'b': 2, 'c': 3}
result = dict.get(key, 'default')


# 2: using a function
def switch(x):
    return {
        '1', 1,
        '2', 2,
        '3', 3,
    }[x]


# 3: using a function with a default (to 0)
def switch(x):
    return {
        '1', 1,
        '2', 2,
        '3', 3,
    }.get(x, 0)


# 4 recreate the classic switch
class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))


while switch(n):
    if case(0):
        print "You typed zero."
        break
    if case(1, 4, 9):
        print "n is a perfect square."
        break
    if case(2):
        print "n is an even number."
    if case(2, 3, 5, 7):
        print "n is a prime number."
        break
    if case(6, 8):
        print "n is an even number."
        break
    print "Only single-digit numbers are allowed."
    break


# 5 classic if/elif/else
if x < 0:
    print('Negative')
elif x == 0:
    print('Zero')
elif x == 1:
    print('One')
else:
    print('More then 1') 