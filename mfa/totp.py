import time
import hmac
import hashlib
import struct
import secrets
from base64 import b32encode, b32decode


def gen(length: int = 10) -> str:
    return b32encode(secrets.token_bytes(length)).decode('utf-8')


def totp(secret: str, t: float = None, digits: int = 6) -> int:
    # Calculate time
    epoch_interval = 30 # TOTP changes every 30 seconds
    if t is None:
        t = time.time()
    current_time = int(t / epoch_interval)
    
    # Get hash code
    msg = struct.pack(">Q", current_time)
    key = b32decode(secret, True)
    hmac_hash = hmac.new(key, msg, hashlib.sha1).digest()
    
    # Get code
    offset = hmac_hash[19] & 15 # Get the last 4 bits of the hash
    binary = (struct.unpack(">I", hmac_hash[offset:offset + 4])[0] & 0x7fffffff) # Get the first 31 bits of the hash
    
    otp = binary % (10 ** digits) # Truncate the hash to the desired number of digits
    return otp


assert len(gen(20)) == 32
assert len(gen(1)) == 8
assert totp('OJMIVD5PYFM7SZKS', t=1741202101.28) == 397337
assert totp('OJMIVD5PYFM7SZKS', t=1741202101.28, digits=4) == 7337
assert totp('OJMIVD5PYFM7SZKS', t=1741202101.28, digits=7) == 8397337