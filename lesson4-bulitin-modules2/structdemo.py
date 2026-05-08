import struct 
import ctypes

## ex1 
# # native byteorder 
# buffer = struct.pack("ihb", 1, 2, 3) 
# print(repr(buffer) )
# print(struct.unpack("ihb", buffer) )
 
# # data from a sequence, network byteorder 
# data = [1, 2, 3] 
# buffer = struct.pack("!ihb", *data)
# print(repr(buffer) )
# print(struct.unpack("!ihb", buffer) )

# # ex2
# var = struct.pack('?hil', True, 2, 5, 445)
# print(var)

# tup = struct.unpack('?hil', var)
# print(tup)

# var = struct.pack('qf', 5, 2.3)
# print(var)

# tup = struct.unpack('qf', var)
# print(tup)

# print(struct.calcsize('?hil'))
# print(struct.calcsize('qf'))


# import struct
# import ctypes

# # Allocate buffer
# size = struct.calcsize('hhl')
# buff = ctypes.create_string_buffer(size)

# # Pack into buffer
# struct.pack_into('hhl', buff, 0, 2, 2, 3)

# # Unpack from buffer
# res = struct.unpack_from('hhl', buff, 0)
# print(res) # (2, 2, 3)

import struct

var = struct.pack('bi', 56, 0x12131415)
print(var)
print(struct.calcsize('bi'))

var = struct.pack('ib', 0x12131415, 56)
print(var)
print(struct.calcsize('ib'))
