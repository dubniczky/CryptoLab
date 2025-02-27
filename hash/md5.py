# This is a python implementation of the MD5 hash algorithm
# The implementation is based on the MD5 algorithm specification: https://tools.ietf.org/html/rfc1321
# The md5 hash function takes in an arbitrary length message and returns a 128-bit hash value


import struct


def _process_chunk(state, chunk):
    assert len(chunk) == 64

    a, b, c, d = state
    
    # Unpack the chunk into 16 32-bit little-endian integers for the transofmations
    x = list(struct.unpack("<16I", chunk))
    
    # Left rotation function
    def rotate_left(x, n): return (x << n) | (x >> (32 - n))

    # Helper functions for the transformation functions
    def F(x, y, z): return (x & y) | (~x & z)
    def G(x, y, z): return (x & z) | (y & ~z)
    def H(x, y, z): return x ^ y ^ z
    def I(x, y, z): return y ^ (x | ~z)

    # Transformation functions, these do the bulk of the work of the irreversible transformation
    def FF(a, b, c, d, x, s, ac):
        a = (a + F(b, c, d) + x + ac) & 0xFFFFFFFF # The & 0xFFFFFFFF is to keep the result as a 32-bit integer
        return (b + rotate_left(a, s)) & 0xFFFFFFFF

    def GG(a, b, c, d, x, s, ac):
        a = (a + G(b, c, d) + x + ac) & 0xFFFFFFFF
        return (b + rotate_left(a, s)) & 0xFFFFFFFF

    def HH(a, b, c, d, x, s, ac):
        a = (a + H(b, c, d) + x + ac) & 0xFFFFFFFF
        return (b + rotate_left(a, s)) & 0xFFFFFFFF

    def II(a, b, c, d, x, s, ac):
        a = (a + I(b, c, d) + x + ac) & 0xFFFFFFFF
        return (b + rotate_left(a, s)) & 0xFFFFFFFF

    # Round 1
    # Each round has 16 steps, one for each of the 16 32-bit integers in the chunk
    # Each step has the same transformation function, but order of inputs and constants
    # The constants come from the MD5 algorithm specification
    a = FF(a, b, c, d, x[0], 7, 0xd76aa478)
    d = FF(d, a, b, c, x[1], 12, 0xe8c7b756)
    c = FF(c, d, a, b, x[2], 17, 0x242070db)
    b = FF(b, c, d, a, x[3], 22, 0xc1bdceee)
    a = FF(a, b, c, d, x[4], 7, 0xf57c0faf)
    d = FF(d, a, b, c, x[5], 12, 0x4787c62a)
    c = FF(c, d, a, b, x[6], 17, 0xa8304613)
    b = FF(b, c, d, a, x[7], 22, 0xfd469501)
    a = FF(a, b, c, d, x[8], 7, 0x698098d8)
    d = FF(d, a, b, c, x[9], 12, 0x8b44f7af)
    c = FF(c, d, a, b, x[10], 17, 0xffff5bb1)
    b = FF(b, c, d, a, x[11], 22, 0x895cd7be)
    a = FF(a, b, c, d, x[12], 7, 0x6b901122)
    d = FF(d, a, b, c, x[13], 12, 0xfd987193)
    c = FF(c, d, a, b, x[14], 17, 0xa679438e)
    b = FF(b, c, d, a, x[15], 22, 0x49b40821)

    # Round 2
    a = GG(a, b, c, d, x[1], 5, 0xf61e2562)
    d = GG(d, a, b, c, x[6], 9, 0xc040b340)
    c = GG(c, d, a, b, x[11], 14, 0x265e5a51)
    b = GG(b, c, d, a, x[0], 20, 0xe9b6c7aa)
    a = GG(a, b, c, d, x[5], 5, 0xd62f105d)
    d = GG(d, a, b, c, x[10], 9, 0x02441453)
    c = GG(c, d, a, b, x[15], 14, 0xd8a1e681)
    b = GG(b, c, d, a, x[4], 20, 0xe7d3fbc8)
    a = GG(a, b, c, d, x[9], 5, 0x21e1cde6)
    d = GG(d, a, b, c, x[14], 9, 0xc33707d6)
    c = GG(c, d, a, b, x[3], 14, 0xf4d50d87)
    b = GG(b, c, d, a, x[8], 20, 0x455a14ed)
    a = GG(a, b, c, d, x[13], 5, 0xa9e3e905)
    d = GG(d, a, b, c, x[2], 9, 0xfcefa3f8)
    c = GG(c, d, a, b, x[7], 14, 0x676f02d9)
    b = GG(b, c, d, a, x[12], 20, 0x8d2a4c8a)

    # Round 3
    a = HH(a, b, c, d, x[5], 4, 0xfffa3942)
    d = HH(d, a, b, c, x[8], 11, 0x8771f681)
    c = HH(c, d, a, b, x[11], 16, 0x6d9d6122)
    b = HH(b, c, d, a, x[14], 23, 0xfde5380c)
    a = HH(a, b, c, d, x[1], 4, 0xa4beea44)
    d = HH(d, a, b, c, x[4], 11, 0x4bdecfa9)
    c = HH(c, d, a, b, x[7], 16, 0xf6bb4b60)
    b = HH(b, c, d, a, x[10], 23, 0xbebfbc70)
    a = HH(a, b, c, d, x[13], 4, 0x289b7ec6)
    d = HH(d, a, b, c, x[0], 11, 0xeaa127fa)
    c = HH(c, d, a, b, x[3], 16, 0xd4ef3085)
    b = HH(b, c, d, a, x[6], 23, 0x04881d05)
    a = HH(a, b, c, d, x[9], 4, 0xd9d4d039)
    d = HH(d, a, b, c, x[12], 11, 0xe6db99e5)
    c = HH(c, d, a, b, x[15], 16, 0x1fa27cf8)
    b = HH(b, c, d, a, x[2], 23, 0xc4ac5665)

    # Round 4
    a = II(a, b, c, d, x[0], 6, 0xf4292244)
    d = II(d, a, b, c, x[7], 10, 0x432aff97)
    c = II(c, d, a, b, x[14], 15, 0xab9423a7)
    b = II(b, c, d, a, x[5], 21, 0xfc93a039)
    a = II(a, b, c, d, x[12], 6, 0x655b59c3)
    d = II(d, a, b, c, x[3], 10, 0x8f0ccc92)
    c = II(c, d, a, b, x[10], 15, 0xffeff47d)
    b = II(b, c, d, a, x[1], 21, 0x85845dd1)
    a = II(a, b, c, d, x[8], 6, 0x6fa87e4f)
    d = II(d, a, b, c, x[15], 10, 0xfe2ce6e0)
    c = II(c, d, a, b, x[6], 15, 0xa3014314)
    b = II(b, c, d, a, x[13], 21, 0x4e0811a1)
    a = II(a, b, c, d, x[4], 6, 0xf7537e82)
    d = II(d, a, b, c, x[11], 10, 0xbd3af235)
    c = II(c, d, a, b, x[2], 15, 0x2ad7d2bb)
    b = II(b, c, d, a, x[9], 21, 0xeb86d391)
    
    return [
        (state[0] + a) & 0xFFFFFFFF,
        (state[1] + b) & 0xFFFFFFFF,
        (state[2] + c) & 0xFFFFFFFF,
        (state[3] + d) & 0xFFFFFFFF
    ]

def hash(data):
    state = [ 0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476 ] # Initial state, as per the MD5 algorithm specification
    
    # Move the data to another buffer it does not modifiy the original data
    buffer = data[:]
    
    # Pad the data
    # The padding consists of a single bit with value 1, followed by zeros, and finally the length of the original message
    # This is the same as the ANSI X.923 padding scheme padding/x923.py
    length = struct.pack("<Q", len(data) * 8) # 8 bits per byte
    buffer += b"\x80" # Add the 1 bit, followed by 7 zeros to make a full byte
    buffer += b"\x00" * ((56 - len(buffer) % 64) % 64) # Pad to 56 bytes to account for the length at the end and the one byte at the start
    buffer += length
    
    # Update the state with the padded data, until there is no more data left
    while len(buffer) >= 64:
        state = _process_chunk(state, buffer[:64]) # Process the first 64 bytes of the buffer
        buffer = buffer[64:] # Remove the processed bytes from the buffer

    return struct.pack("<4I", *state) # Create a byte string from the integers


assert hash(b'hello').hex() == "5d41402abc4b2a76b9719d911017c592"
assert hash(b'').hex() == "d41d8cd98f00b204e9800998ecf8427e"
