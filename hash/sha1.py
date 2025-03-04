# This is a python implementation of the SHA1 hash algorithm
# The implementation is based on the SHA1 algorithm specification: https://tools.ietf.org/html/rfc1321
# The md5 hash function takes in an arbitrary length message and returns a 128-bit hash value


import struct


def _left_rotate(n, b):
        return ((n << b) | (n >> (32 - b))) & 0xffffffff

def sha1(data: bytes) -> str:
    # Initialize default hash values. These values are the first 32 bits of the fractional parts of the square roots of the first 8 prime numbers. This does not have any special meaning, but it is a simple way to get a set of initial values that are not too predictable.
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0
    
    # Pad the message to a multiple of 512 bits (64 bytes) and the length of the message at the end
    # This is similar to the ANSI X.923 padding scheme, except the first byte is 0x80 instead of 0x00 (1000 0000 in binary)
    data_byte_size = len(data) * 8
    data += b'\x80'
    while (len(data) % 64) != 56: # (64-8) Leave 8 bytes at the end for the length of the message
        data += b'\x00'
    data += struct.pack('>Q', data_byte_size) # Create a number with the length of the original data in bits and pack it as a 64-bit big-endian integer

    # Process the messages in 64 byte chunks
    for i in range(0, len(data), 64):
        w = [0] * 80
        # Convert the 64 byte chunk into 16 32-bit big-endian integers
        for j in range(16):
            w[j] = struct.unpack('>I', data[i + j*4:i + j*4 + 4])[0]
        for j in range(16, 80):
            w[j] = _left_rotate(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1)

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= j <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (_left_rotate(a, 5) + f + e + k + w[j]) & 0xffffffff
            e = d
            d = c
            c = _left_rotate(b, 30)
            b = a
            a = temp

        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff

    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)


assert sha1(b'abcd') == '81fe8bfe87576c3ecb22426f8e57847382917acf'
assert sha1(b'') == 'da39a3ee5e6b4b0d3255bfef95601890afd80709'
