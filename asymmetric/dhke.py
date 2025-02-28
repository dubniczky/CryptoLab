import random
import secrets
from sympy import nextprime


# Generator to use, which must be a primitive root modulo p
# Since 5 is a prime, it is fine to use with any prime p (except 5)
g = 5
# Prime number for the size of the group
# 1024 bits is a common size for DHKE
bits = 1024
# Prime number to use as the modulus
# Generate a random prime number of the specified size
p = nextprime(secrets.randbits(bits))

# Generate a private key for alice
a = random.randint(1, p - 1) # Any number below p is fine
A = pow(g, a, p) # Alice's public key

# Generate a private key for bob
b = random.randint(1, p - 1) # Any number below p is fine
B = pow(g, b, p) # Bob's public key

# Calculate the shared secret
sb = pow(A, b, p) # Shared secret for bob
sa = pow(B, a, p) # Shared secret for alice

assert sa == sb
