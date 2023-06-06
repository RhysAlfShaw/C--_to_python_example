import ctypes
import time
# Load the shared library
square_lib = ctypes.CDLL('./square.so')
add_one_lib = ctypes.CDLL('./add_one.so')

# Specify the function return type
square_lib.square.restype = ctypes.c_int
add_one_lib.addOneLoop.restype = ctypes.c_int
add_one_lib.addOneLoop.argtypes = [ctypes.c_int, ctypes.c_int]

def squarepy(number):
    return number**2

def add_one(number,i):
    for i in range(i):
        number += 1
    return number

import timeit

starting_number = 5
iterations = 1000000

# now we see some speed-up!
t = timeit.Timer(lambda: add_one_lib.addOneLoop(starting_number,iterations))
print('C++',t.timeit(number=1_000))

t = timeit.Timer(lambda: add_one(starting_number,iterations))
print('Python',t.timeit(number=1_000))


