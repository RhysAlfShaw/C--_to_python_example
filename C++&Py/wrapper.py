import ctypes
import time

# Load the shared library (the .so file) into c_types.
add_one_lib = ctypes.CDLL('./add_one.o')

# Specify the function return type
add_one_lib.addOneLoop.restype = ctypes.c_int
add_one_lib.multiply.restype = ctypes.c_int
add_one_lib.addOneLoop.argtypes = [ctypes.c_int, ctypes.c_int]
add_one_lib.multiply.argtypes = [ctypes.c_int, ctypes.c_int]

def squarepy(number):
    return number**2

def add_one(number,i):
    for i in range(i):
        number += 1
    return number

import timeit

starting_number = 5
iterations = 100_000_000

# now we see some speed-up! The more we do in C++, the more speed-up we see.
# The initalization over head is reduced.
t = timeit.Timer(lambda: add_one_lib.addOneLoop(starting_number,iterations))
print('C++ :',t.timeit(number=1))

t = timeit.Timer(lambda: add_one(starting_number,iterations))
print('Python :',t.timeit(number=1))

# test the multiplication function

a = 5
b = 10

print('C++ :',add_one_lib.multiply(a,b))