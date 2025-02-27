# Tiny Encryption Algorithm (TEA) implementation in Python.
# TEA is a block cipher with a block size of 64 bits and a key size of 128 bits.
# TEA operates on 64-bit blocks using a 128-bit key. The block is divided into two 32-bit halves (L and R) which are added to the key in a number of rounds in a feistel-like manner.
# TEA is not secure for use in cryptographic applications, as it is vulnerable to a number of attacks, including differential cryptanalysis.
# The decryption function is the same as the encryption function, except that the order of the subkeys is reversed.


def encrypt(v, key, rounds=32, delta=0x9E3779B9) -> tuple[int, int]:
    '''Encrypt an 8 byte block using the Tiny Encryption Algorithm (TEA).'''
    v0, v1 = v[0], v[1]
    sum_ = 0
    k0, k1, k2, k3 = key
    for _ in range(rounds):
        sum_ = (sum_ + delta) & 0xFFFFFFFF
        v0 += ((v1 << 4) + k0) ^ (v1 + sum_) ^ ((v1 >> 5) + k1)
        v0 &= 0xFFFFFFFF
        v1 += ((v0 << 4) + k2) ^ (v0 + sum_) ^ ((v0 >> 5) + k3)
        v1 &= 0xFFFFFFFF
    return v0, v1

def decrypt(v, key, rounds=32, delta=0x9E3779B9) -> tuple[int, int]:
    '''Decrypt an 8 byte block that was encrypted using the Tiny Encryption Algorithm (TEA).'''
    v0, v1 = v[0], v[1]
    sum_ = (rounds * delta) & 0xFFFFFFFF
    k0, k1, k2, k3 = key
    for _ in range(rounds):
        v1 -= ((v0 << 4) + k2) ^ (v0 + sum_) ^ ((v0 >> 5) + k3)
        v1 &= 0xFFFFFFFF
        v0 -= ((v1 << 4) + k0) ^ (v1 + sum_) ^ ((v1 >> 5) + k1)
        v0 &= 0xFFFFFFFF
        sum_ = (sum_ - delta) & 0xFFFFFFFF
    return v0, v1


assert decrypt(encrypt((0x12345678, 0x9ABCDEF0), (0xA56BABCD, 0x00000000, 0x00000000, 0x00000000)), (0xA56BABCD, 0x00000000, 0x00000000, 0x00000000)) == (0x12345678, 0x9ABCDEF0)