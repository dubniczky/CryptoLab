# This module implements the CRC-32 algorithm, ISO-HDLC version.
# The CRC-32 algorithm is a widely used checksum algorithm that is used in ethernet, zip files, and many other applications.
# The algorithm is simple: it XORs the next byte with the CRC, and then shifts the CRC right 8 times, XORing with 0xEDB88320 if the least significant bit is set.
# It is not cryptographically secure, but it is fast and easy to implement.


def hash(data: bytes) -> int:
    crc = 0xFFFFFFFF # 4 bytes of 1s
    for byte in data:
        crc ^= byte # XOR with the next byte
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xEDB88320 # 0xEDB88320 is the reversed polynomial
            else:
                crc >>= 1
    return crc ^ 0xFFFFFFFF

assert hash(b"abcdefgh") == 0xAEEF2A50
