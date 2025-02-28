import random
import secrets
from sympy import nextprime


def gen(bits: int) -> int:
    prime_candidate = secrets.randbits(bits)
    return nextprime(prime_candidate)

def private(prime: int) -> int:
    return random.randint(1, prime - 1)

def public(prime: int, base: int, private_key: int) -> int:
    return pow(base, private_key, prime)


assert (g := 5)
assert (p := gen(1024))
assert (a := private(p))
assert (A := public(p, g, a))
assert (b := private(p))
assert (B := public(p, g, b))
assert public(p, B, a) == public(p, A, b)
