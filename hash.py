from bitarray import bitarray
from bitarray.util import *

bit_count = 160

def wrap_bitarray(bitarray):
    integer_value = ba2int(bitarray, signed=False)
    if integer_value > (2 ** bit_count - 1):
        bitarray = int2ba(integer_value % (2 ** bit_count - 1) - 1, length=bit_count)
    return bitarray

def wrap_int(integer):
    if integer > (2 ** bit_count - 1):
        return integer % (2 ** bit_count - 1) - 1
    return integer

def leftshift(ba, count):
    return ba[count:] + (bitarray('0') * count)

def rightshift(ba, count):
    return (bitarray('0') * count) + ba[:-count]

def hash_function(string):
    # Preprocessing
    processed_string = bitarray()
    processed_string.frombytes(string.encode('ascii'))
    if(len(processed_string) % bit_count != 0):
        to_append = bytearray(bit_count - len(processed_string) % bit_count)
        processed_string.extend(to_append)

    # Initial internal state
    internal_state = hex2ba('67452301EFCDAB8998BADCFE10325476C3D2E1F0')

    # Process string in chunks of bit_count bits
    current_bit = 0
    while(current_bit != len(processed_string)):
        internal_state = wrap_bitarray(processed_string[current_bit : current_bit + bit_count] + rightshift(internal_state, 2))
        internal_state = wrap_bitarray(int2ba(wrap_int(ba2int(internal_state, signed=False) * 499979), length=bit_count))
        internal_state = internal_state | int2ba(543, length=bit_count)
        internal_state = wrap_bitarray(int2ba(wrap_int(ba2int(internal_state, signed=False) * 81667), length=bit_count))
        internal_state = leftshift(internal_state, 2)

        current_bit += bit_count
    
    return ba2hex(internal_state)
