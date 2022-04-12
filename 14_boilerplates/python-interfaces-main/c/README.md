1. Create C file with some function

    ```C
    #include <stdio.h>
    
    int square(int i) {
        return i * i;
    }
    ```

2. Compile the file. In Windows with GCC you can 
    
    `gcc -shared -o libmodule.so libmodule.c`

3. Use it from Python.

```python
import ctypes
clib = ctypes.CDLL('libmodule.so')  # compiled file
print(clib.square(8))
```