import ctypes

functions = ctypes.CDLL('libmodule.so')
print(functions.square(8))
