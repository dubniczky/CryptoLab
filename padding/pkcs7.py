# The PKCS#7 padding scheme is a simple padding scheme that pads the message with a number of bytes to make the message length a multiple of the block size. The value of each byte that is added is the number of bytes that are added. For example, if the block size is 8 bytes and the message is 10 bytes long, then 6 bytes are added, each with the value 6. If the message is already a multiple of the block size, then an entire block of padding is added. If the message is one byte short of being a multiple of the block size, then one byte of padding is added, with the value 1. The PKCS#7 padding scheme is used in many cryptographic protocols, including SSL/TLS and IPsec.
# A limitation is that the block size must be between 1 and 256 bytes, inclusive. This is because the padding length is stored in a single byte, and the maximum value of a byte is 255. Additionally this padding scheme always adds padding, even if the message is already a multiple of the block size. This can be an issue for small messages, as the padding can effectively double the block size.


def pad(data: bytes, block_size: int) -> bytes | None:
    if block_size < 1 or block_size > 256:
        return None
    pad_len = block_size - (len(data) % block_size)
    return data + bytes([pad_len] * pad_len)

def unpad(data: bytes) -> bytes | None:
    pad_len = data[-1]
    if pad_len < 1 or pad_len > len(data):
        return None
    return data[:-pad_len]


assert pad(b'hello', 8) == b'hello\x03\x03\x03'
assert pad(b'welcome stranger', 8) == b'welcome stranger\x08\x08\x08\x08\x08\x08\x08\x08'
assert pad(b'welcome stranger!', 8) == b'welcome stranger!\x07\x07\x07\x07\x07\x07\x07'
assert pad(b'', 4) == b'\x04\x04\x04\x04'
assert unpad(b'\x02\x02\x02\x02') == b'\x02\x02'
assert unpad(pad(b'hello', 8)) == b'hello'
assert unpad(pad(b'this is a long message, taking up multiple blocks', 4)) == b'this is a long message, taking up multiple blocks'