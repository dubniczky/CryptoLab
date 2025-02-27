# Description: ISO 7816-4 padding implementation.
# The ISO 7816-4 padding is a simple padding scheme that pads the message with a single 0x80 byte (1000000 in binary) followed by zero or more 0x00 bytes to make the message length a multiple of the block size. This padding scheme is used in smart cards and other applications that require compatibility with ISO 7816-4. The idea is that you start searching from the back for the first 1 bit, which is at the start of one of the bytes. One advantage of this method is that it can work with data that doees not end in a full byte.


def pad(data: bytes, block_size: int) -> bytes | None:
    '''Pad the data using the ISO 7816-4 padding scheme.'''
    if block_size < 1:
        return None # Invalid block size
    pad_len = block_size - (len(data) % block_size)
    if pad_len == 0:
        pad_len = block_size
    return data + b'\x80' + b'\x00' * (pad_len - 1)

def unpad(data: bytes) -> bytes | None:
    '''Unpad the data using the ISO 7816-4 padding scheme.'''
    # Find the last occurrence of 0x80 and remove it and any trailing zeros.
    index = data.rfind(b'\x80')
    if index == -1:
        return None
    return data[:index]


assert pad(b'hello', 8) == b'hello\x80\x00\x00'
assert pad(b'123', 4) == b'123\x80'
assert pad(b'1234', 4) == b'1234\x80\x00\x00\x00'
assert pad(b'welcome stranger', 8) == b'welcome stranger\x80\x00\x00\x00\x00\x00\x00\x00'
assert pad(b'welcome stranger!', 8) == b'welcome stranger!\x80\x00\x00\x00\x00\x00\x00'
assert pad(b'', 4) == b'\x80\x00\x00\x00'
assert unpad(b'\x00\x00\x80\x00') == b'\x00\x00'
assert unpad(pad(b'hello', 8)) == b'hello'
assert unpad(pad(b'this is a long message, taking up multiple blocks', 4)) == b'this is a long message, taking up multiple blocks'