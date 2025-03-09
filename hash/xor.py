# The XOR hash is an easy to implement hash function that is not cryptographically secure.
# It accepts and arbitrary length message and returns a single byte hash value.
# The hash value is calculated by XORing all the bytes in the message together.


def hash(data: bytes) -> int:
    result = 0xFF
    for byte in data:
        result ^= byte
    return result


assert hash(b'abcd') == 251
assert hash(b'') == 255
assert hash(b'Deep in the Hundred Acre Wood, Where Christopher Robin plays, You\'ll find the enchanted neighborhood, Of Christopher\'s childhood days') == 209
