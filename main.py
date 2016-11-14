from ctypes import *
from sys import platform

def create_ffi_uuid_v4():
    if platform == 'darwin':
        prefix = 'lib'
        ext = 'dylib'
    elif platform == 'win32':
        prefix = ''
        ext = 'dll'
    else:
        prefix = 'lib'
        ext = 'so'

    lib = cdll.LoadLibrary('target/release/{}ffi_uuidv4.{}'.format(prefix, ext))
    generate_uuid_v4 = lib.generate_uuid_v4
    generate_uuid_v4.restype = c_char_p
    return generate_uuid_v4


uuid_v4 = create_ffi_uuid_v4()
result = []
for i in range(1,100000):
    v = uuid_v4()
    result.append(v)

print('{}'.format(result[100]))
