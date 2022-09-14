import os.path
import sys
from cffi import FFI


ffi = FFI()
ffi.cdef(
    open(
        os.path.join(
            # FIXME: path is hard-coded
            os.path.dirname(__file__),
            'src',
            'hellorust.h',
        )
    ).read()
)

if sys.platform == 'win32':
    DYNAMIC_LIB_FORMAT = '%s.dll'
elif sys.platform == 'darwin':
    DYNAMIC_LIB_FORMAT = 'lib%s.dylib'
else:
    DYNAMIC_LIB_FORMAT = 'lib%s.so'

rust_lib = ffi.dlopen(
    os.path.join(
        os.path.dirname(__file__),
        'target',
        'release',
        DYNAMIC_LIB_FORMAT % 'hellorust',
    )
)


def main():
    assert rust_lib.hello(b"Python") == 42


if __name__ == '__main__':
    main()
