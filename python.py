import cffi

ffi = cffi.FFI()

ffi.cdef('''
    uint32_t add(uint32_t left, uint32_t right);
''')

C = ffi.dlopen('target/debug/libpython_rust_example.so')

print(C)
print(dir(C))
print(C.add)
print(C.add(1, 2))
