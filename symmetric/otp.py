# One time pad (OTP) encryption is a method of encryption that is theoretically unbreakable if used correctly. It involves generating a random key that is as long as the message to be encrypted. The key is then XORed with the message to produce the ciphertext. The key is never reused, and the key is kept secret from anyone who should not be able to decrypt the message.
# The limitation here is that the key must be as long as the message, and it must be truly random. If the key is not random or if it is reused, the encryption can be broken. This makes OTP encryption impractical for most real-world applications.


def encrypt(key: bytes, data: bytes) -> bytes:
    '''Encrypts the plaintext using the key as a one time pad.'''
    if len(key) != len(data):
        raise ValueError("Key and data must be the same length")
    return bytes( [ a ^ b for a, b in zip(key, data) ] )

def decrypt(key: bytes, data: bytes) -> bytes:
    '''Decrypts the ciphertext using the key as a one time pad.'''
    return encrypt(key, data) # XOR is its own inverse, so encryption and decryption are the same


assert decrypt(b"abcdef", encrypt(b"abcdef", b"mangos")) == b"mangos"
