from bitarray import bitarray
from bitarray.util import *

bit_count = 256
def wrap_value(bitarray):
    integer_value = ba2int(bitarray, signed=False)
    if integer_value > (2 ** bit_count - 1):
        bitarray = int2ba(integer_value % (2 ** bit_count - 1) - 1, length=bit_count)
    return bitarray

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
    #internal_state = hex2ba('67452301EFCDAB8998BADCFE10325476C3D2E1F0')
    internal_state = hex2ba('67452301')

    # Process string in chunks of bit_count bits
    current_bit = 0
    while(current_bit != len(processed_string)):
        internal_state = wrap_value(processed_string[current_bit : current_bit + bit_count] + rightshift(internal_state, 2))
        internal_state = wrap_value(int2ba(ba2int(internal_state, signed=False) + 499979, length=bit_count))
        current_bit += bit_count
    
    return ba2hex(internal_state)

print(hash_function('Atas asas sa eos et asslick et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores assdick consequatur aut perferendis doloribus asperiores repellat.'))