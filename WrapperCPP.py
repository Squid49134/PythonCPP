import ctypes
import numpy as np
from numpy.ctypeslib import ndpointer


# The path to the library file
libPath   = "D:\\Kellie and Billy\\Documents\\Python\\C++ Wrapper\\FunctionsCPP.so"
#libPath = "D:\\Kellie and Billy\\Documents\\Visual Studio 2019\\Projects\\ScatterAccel\\x64\\Debug\\ScatterAccel.dll"
# importing the library
library = ctypes.cdll.LoadLibrary(libPath)


def Add(num1, num2):
    # Identifying the C++ function
    func          = library.AddCPP  # name
    func.restype  = ctypes.c_double  # double return type
    func.argtypes = [ctypes.c_double, ctypes.c_double]  # 2 doubles parameters to pass by value
    
    # Calling the C++ function
    return func(num1, num2)

print(Add(1.0, 1.0))
print('')


def MultByTwo(numArr):
    # Identifying the C++ function
    func          = library.MultByTwoCPP  # Name
    func.restype  = int  # void return Type
    func.argtypes = [ndpointer(ctypes.c_double), ctypes.c_uint]  # double pointer and unsigned integer array length to pass by reference
    
    # Calling the C++ function
    func(numArr, len(numArr))
    
    return numArr

array = np.zeros(5)
for i in range(0, 5):
    array[i] = i + 1.0
print(MultByTwo(array))
print('')


def MultByTwo2D(numArr, xDim, yDim):
    # Identifying the C++ function
    func          = library.MultByTwo2DCPP  # Name
    func.restype  = int  # void return Type
    func.argtypes = [ndpointer(ctypes.c_double), ctypes.c_uint, ctypes.c_uint]  # double pointer and 2 unsigned integer array dimensions to pass by reference
    
    # packing the 2D array into a 1D array to pass as simple pointer
    packedArr = np.resize(array2D, (xDim * yDim))
    # Calling the C++ function
    func(packedArr, xDim, yDim)
    # unpacking the returned 1D array into the original 2D dimmensions
    unpackedArr = np.resize(packedArr, (yDim, xDim))
    
    return unpackedArr

xDim = 3
yDim = 4
array2D = np.zeros((yDim, xDim))
for j in range(0, yDim):
    for i in range(0, xDim):
        array2D[j][i] = j * xDim + i + 1
print(MultByTwo2D(array2D, xDim, yDim))


