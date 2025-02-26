# Feistel cipher with SHA-256 as the round function.

# A feistel cipher is a symmetric structure used to build block ciphers. It is based on the concept of a round function, which is a function that takes a key and a block of data and returns a new block of data. The round function is applied multiple times to the data in a specific way to produce the final encrypted or decrypted data. Usually it alterates between applying the round function to the left and right halves of the data. To decrypt the data, the round function is applied in reverse order.
# https://en.wikipedia.org/wiki/Feistel_cipher

import hashlib


def encrypt(key: bytes, block: bytes, rounds=16) -> bytes:
    '''Encrypts a block of 32 bytes using a feistel cipher with SHA-256 as the round function.'''
    left = block[ : len(block)//2 ]
    right = block[ len(block)//2 : ]
    for i in range(rounds):
        f = hashlib.sha256(right + key + bytes(i)).digest()[:len(right)]
        new_right = bytes( [a ^ b for a, b in zip(f, left)] )
        left, right = right, new_right
    return left + right

def decrypt(key: bytes, block: bytes, rounds=16) -> bytes:
    '''Decrypts a block of 32 bytes using a feistel cipher with SHA-256 as the round function.'''
    left = block[:len(block)//2]
    right = block[len(block)//2:]
    for i in range(rounds-1, -1, -1):
        f = hashlib.sha256(left + key + bytes(i)).digest()[:len(right)]
        new_left = bytes([a ^ b for a, b in zip(f, right)])
        right, left = left, new_left
    return left + right


assert decrypt(b'password123', encrypt(b'password123', b'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')) == b'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
