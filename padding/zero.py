# Zero padding is a simple padding scheme that pads the input with zeros.
# Zero padding is irreversible if the original data can end with one or more zeros, as the padding cannot be distinguished from the original data. For data that cannot contain zeros, such as text, zero padding is reversible.


def pad(data: bytes, block_size: int, b: bytes = b'\x00') -> bytes:
    if len(data) > 0 and len(data) % block_size == 0:
        # If the data is already a multiple of the block size, we don't need to pad it, except if the data is empty
        return data
    padding = block_size - len(data) % block_size
    return data + b * padding

def unpad(data: bytes, b: bytes = b'\x00') -> bytes:
    return data.rstrip(b)


assert pad(b'hello', 8) == b'hello\x00\x00\x00'
assert pad(b'welcome stranger', 8) == b'welcome stranger'
assert pad(b'welcome stranger!', 8) == b'welcome stranger!\x00\x00\x00\x00\x00\x00\x00'
assert pad(b'', 4) == b'\x00\x00\x00\x00'
assert unpad(b'\x00\x00') == b''
assert unpad(pad(b'hello', 8)) == b'hello'