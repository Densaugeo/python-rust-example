# Python Rust Example

This is an attempt to create a working example of calling Rust code from Python.

## Overview

I'd like to be able to call Rust functions from Python, but have not foudn any working examples for this. Most of the examples I can find are for C.

The example in the PYO3 repo sort-of works, but breaks if anything at all is changed (even the name of the folder the project is built in). Additionally, it uses opaque mechanisms and I can't figure out how to modify the Python modules it produces or how they work.

## Current State

Rust components can be built using `cargo` and the example script can be run using `python`, but calling the Rust function does not work:

```
$ cargo build
$ python python.py
<cffi.api._make_ffi_library.<locals>.FFILibrary object at 0x7fbc17e26960>
[]
Traceback (most recent call last):
  File "/home/den-antares/projects/python-rust/python.py", line 13, in <module>
    print(C.add)
          ^^^^^
  File "/usr/lib64/python3.12/site-packages/cffi/api.py", line 912, in __getattr__
    make_accessor(name)
  File "/usr/lib64/python3.12/site-packages/cffi/api.py", line 907, in make_accessor
    raise AttributeError(name)
AttributeError: add
```

## Sources

https://cffi.readthedocs.io/en/latest/overview.html#other-cffi-modes
https://stackoverflow.com/questions/65246103/using-cffi-to-call-functions-of-shared-library-from-python
https://blog.ian.stapletoncordas.co/2018/01/making-python-faster-with-rust-and-cffi-or-not.html
https://www.reddit.com/r/rust/comments/7w6sel/help_call_python_defined_function_from_rust_via/
https://github.com/PyO3/pyo3
