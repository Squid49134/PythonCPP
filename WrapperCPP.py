import ctypes
import numpy as np
from numpy.ctypeslib import ndpointer


# The path to the library file
libPath   = "D:\\Kellie and Billy\\Documents\\Python\\C++ Wrapper\\FunctionsCPP.so"
# importing the library
library = ctypes.cdll.LoadLibrary(libPath)


def Add(num1, num2):
    # Identifying the C++ function
    func          = library.AddCPP  # name
    func.restype  = ctypes.c_double  # double return type
    func.argtypes = [ctypes.c_double, ctypes.c_double]  # 2 doubles parameters to pass by value
    
    # Calling the C++ function
    return func(num1, num2)

def MultByTwo(numArr):
    # Identifying the C++ function
    func          = library.MultByTwoCPP  # Name
    func.restype  = int  # void return Type
    func.argtypes = [ndpointer(ctypes.c_double), ctypes.c_uint]  # double pointer and unsigned integer array length to pass by reference
    
    # Calling the C++ function
    func(numArr, len(numArr))
    
    return numArr



print(Add(1.0, 1.0))

array = np.zeros(5)
for i in range(0, 5):
    array[i] = i + 1.0
print(MultByTwo(array))