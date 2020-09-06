from bitarray import bitarray
from bitarray.util import *

def wrap_value(bitarray):
    integer_value = ba2int(bitarray, signed=False)
    if integer_value > 2 ** 160:
        bitarray = int2ba(integer_value % 2 ** 160, length=160)
        return bitarray
    return bitarray

def leftshift(ba, count):
    return ba[count:] + (bitarray('0') * count)

def rightshift(ba, count):
    return (bitarray('0') * count) + ba[:-count]

def hash_function(string):
    # Preprocessing
    processed_string = bitarray()
    processed_string.frombytes(string.encode('ascii'))

    # Initial internal state
    internal_state = hex2ba('67452301EFCDAB8998BADCFE10325476C3D2E1F0')

    # Process string in chunks of 160 bits
    current_bit = 0
    while(current_bit != len(processed_string)):
        internal_state = internal_state ^ processed_string[current_bit : current_bit + 160]
        internal_state = internal_state | processed_string[current_bit : current_bit + 160]
        internal_state = wrap_value(internal_state + processed_string[current_bit : current_bit + 160])
        internal_state = leftshift(internal_state, 2)
        internal_state = rightshift(internal_state, 4)
        current_bit += 160

    return ba2hex(internal_state)

print(hash_function('zullpuclpullpulldullpulxpullpullxxxxpulz'))