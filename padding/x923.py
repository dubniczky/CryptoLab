# Padding scheme: ANSI X.923
# The ANSI X.923 padding scheme is a simple padding scheme that pads the message with a number of bytes to make the message length a multiple of the block size. The value of each byte that is added is zero, except for the last byte, which is the number of bytes that are added. For example, if the block size is 8 bytes and the message is 10 bytes long, then 6 bytes are added, each with the value 0, and the last byte is 6. If the message is already a multiple of the block size, then an entire block of padding is added. If the message is one byte short of being a multiple of the block size, then one byte of padding is added, with the value 1. The ANSI X.923 padding scheme is used in many cryptographic protocols, including DES and AES.


def pad(data: bytes, block_size: int) -> bytes | None:
    if block_size < 1 or block_size > 256:
        return None # Invalid block size
    pad_len = block_size - (len(data) % block_size)
    if pad_len == 0:
        pad_len = block_size
    return data + b'\x00' * (pad_len - 1) + bytes([pad_len])

def unpad(data: bytes) -> bytes | None:
    pad_len = data[-1]
    if pad_len < 1 or pad_len > len(data):
        return None # Invalid padding
    return data[:-pad_len]


assert pad(b'hello', 8) == b'hello\x00\x00\x03'
assert pad(b'123', 4) == b'123\x01'
assert pad(b'1234', 4) == b'1234\x00\x00\x00\x04'
assert pad(b'welcome stranger', 8) == b'welcome stranger\x00\x00\x00\x00\x00\x00\x00\x08'
assert pad(b'welcome stranger!', 8) == b'welcome stranger!\x00\x00\x00\x00\x00\x00\x07'
assert pad(b'', 4) == b'\x00\x00\x00\x04'
assert unpad(b'\x00\x00\x00\x02') == b'\x00\x00'
assert unpad(pad(b'hello', 8)) == b'hello'
assert unpad(pad(b'this is a long message, taking up multiple blocks', 4)) == b'this is a long message, taking up multiple blocks'