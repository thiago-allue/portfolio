# Rust

`cargo new rusty --bin`

`cargo new rusty --lib`

`cargo build`

`cargo build --release`

## Python

```python
import pathlib
import ctypes

lib = ctypes.WinDLL(str(pathlib.Path().parent.joinpath('target', 'release', 'embed.dll')))
print(lib.is_prime(7))
print('Done')
```

```python
from ctypes import cdll

lib = cdll.LoadLibrary('target/release/libembed.so')
lib.function()
print("Execution done")
```

## Resources

- https://doc.rust-lang.org/1.2.0/book/rust-inside-other-languages.html
- https://github.com/dgrunwald/rust-cpython
- https://pypi.org/project/setuptools-rust/