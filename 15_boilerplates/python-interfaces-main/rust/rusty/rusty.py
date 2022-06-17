import pathlib
import ctypes

lib = ctypes.WinDLL(str(pathlib.Path().parent.joinpath('target', 'release', 'embed.dll')))
print(lib.is_prime(7))
print('Done')
