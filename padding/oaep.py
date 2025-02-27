# Padding: Optimal Asymmetric Encryption Padding (OAEP)
# OAEP is used primarily with RSA encryption. It’s designed to prevent certain attacks by introducing randomness in a deterministic, reversible way. Instead of simply appending a fixed pattern, OAEP combines a hash (of an optional label), a randomly generated seed, and a mask generation function (MGF) to “pad” the message into a fixed-length block.
# The disadvantage of this padding is that it can only prduce a single block of output of a limited size, as well as the overhead of the padding process itself copared to th simpler paddings.

import secrets
import hashlib


def _mgf1(seed: bytes, mask_len: int, hash_function=hashlib.sha256) -> bytes:
    '''Mask Generation Function based on a hash function.'''
    mask = b''
    counter = 0
    while len(mask) < mask_len:
        C = counter.to_bytes(4, 'big')
        mask += hash_function(seed + C).digest()
        counter += 1
    return mask[:mask_len]

def pad(message: bytes, k: int, label: bytes = b"", hash_function=hashlib.sha256) -> bytes | None:
    """
    OAEP padding for RSA.
    k: intended length in bytes of the encoded message (typically RSA modulus size in bytes)
    """
    hash_length = hash_function().digest_size
    m_length = len(message)
    if m_length > k - 2 * hash_length - 2:
        return None # The message is too long
    
    l_hash = hash_function(label).digest()
    ps = b'\x00' * (k - m_length - 2 * hash_length - 2)
    db = l_hash + ps + b'\x01' + message
    seed = secrets.token_bytes(hash_length)
    dbMask = _mgf1(seed, k - hash_length - 1, hash_function)
    maskedDB = bytes(x ^ y for x, y in zip(db, dbMask))
    seedMask = _mgf1(maskedDB, hash_length, hash_function)
    maskedSeed = bytes(x ^ y for x, y in zip(seed, seedMask))
    return b'\x00' + maskedSeed + maskedDB

def unpad(encoded_message: bytes, k: int, label: bytes = b"", hash_function=hashlib.sha256) -> bytes:
    """
    OAEP unpadding for RSA.
    k: intended length in bytes of the encoded message (typically RSA modulus size in bytes)
    """
    hash_length = hash_function().digest_size
    if len(encoded_message) != k or k < 2 * hash_length + 2:
        raise ValueError("Invalid encoded message")
    
    maskedSeed = encoded_message[1:hash_length+1]
    maskedDB = encoded_message[hash_length+1:]
    seedMask = _mgf1(maskedDB, hash_length, hash_function)
    seed = bytes(x ^ y for x, y in zip(maskedSeed, seedMask))
    dbMask = _mgf1(seed, k - hash_length - 1, hash_function)
    db = bytes(x ^ y for x, y in zip(maskedDB, dbMask))
    l_hash = hash_function(label).digest()
    l_hash2 = db[:hash_length]
    if l_hash != l_hash2:
        raise ValueError("Invalid label hash")
    i = hash_length
    while i < len(db) and db[i] == 0:
        i += 1
    if db[i] != 1:
        raise ValueError("Invalid padding")
    return db[i+1:]

# For example, k = 128 for a 1024-bit RSA key (128 bytes)
assert unpad( pad(b"advanced padding", 128), 128) == b"advanced padding"
assert unpad( pad(b"012345678", 128), 128) == b"012345678"
assert pad(b"0123456789aaa", 64) == None
assert unpad( pad(b"123456", 128), 128) == b"123456"
assert unpad( pad(b"", 128), 128) == b""
