# Functions syntax

# Variable
a = "Ilya"

# simple functions
def func(name):
    print(f"Hello, {name}")

def do_operations(a, b, do):
    result = do(a, b)
    print(f"result = {result}")

def sum(a, b):
    return a + b

def multiply(a, b): return a * b

do_operations(5, 4, sum)


