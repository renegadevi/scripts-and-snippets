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




###############################################################################
# Additional solutions from the e-book "Python - Notes for Professionals"
# http://books.goalkicker.com/PythonBook/
###############################################################################

##########################################################
# 1: Use what the language offers: the if/else construct
##########################################################
def switch(value):
    if value == 1:
        return "one"
    if value == 2:
        return "two"
    if value == 42:
        return "the answer to the question about life, the universe and everything"
    raise Exception("No case found!")

switch(1)  # one
switch(2)  # two
switch(3)  # Exception: No case found!
switch(42) # the answer to the question about life the universe and everything

##########################################################
# 2: Use a dict of functions
##########################################################
switch = {
    1: lambda: 'one',
    2: lambda: 'two',
    42: lambda: 'the answer of life the universe and everything',
}
def default_case():
    raise Exception('No case found!')

switch.get(1, default_case)() # one
switch.get(2, default_case)() # two
switch.get(3, default_case)() # Exception: No case found
switch.get(42, default_case)() # the answer of life the universe and everything

# 2-2: make some syntactic sugar so the switch looks nicer
def run_switch(value):
    return switch.get(value, default_case)()

run_switch(1) # one

##########################################################
# 3: Use class introspection
##########################################################
class SwitchBase:
    def switch(self, case):
        m = getattr(self, 'case_{}'.format(case), None)
        if not m:
            return self.default
        return m

    __call__ = switch

class CustomSwitcher:

    def case_1(self):
        return 'one'

    def case_2(self):
        return 'two'

    def case_42(self):
        return 'the answer of life, the universe and everything!'

    def default(self):
        raise Exception('Not a case!')

switch = CustomSwitcher()
print(switch(1)) # one
print(switch(2)) #two
print(switch(3)) # Exception: Not a case!
print(switch(42)) # the answer of life, the universe and everything!

##########################################################
# 4: Using a context manager
##########################################################
class Switch:
    def __init__(self, value):
        self._val = value

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return False # Allows traceback to occur

    def __call__(self, cond, *mconds):
        return self._val in (cond,)+mconds

def run_switch(value):
    with Switch(value) as case:
        if case(1):
            return 'one'

        if case(2):
            return 'two'

        if case(3):
            return 'the answer to the question about life, the universe and everything'
    # default
    raise Exception('Not a case!')


run_switch(1) # one
run_switch(2) # two
run_switch(3) # Exception: Not a case!
run_switch(42) # the answer to the question about life, the universe and everything

