import os

# urandom is a cryptographically secure random number generator provided by the OS.
# The main disadvantage of using urandom is that it is slow compared to other random number generators.

def token(n: int) -> bytes:
    '''Return n number of random bytes using urandom.'''
    return os.urandom(n)

def random() -> float:
    '''Generates a random float between 0 and 1 using urandom.'''
    return int.from_bytes(token(8), "big") / (2**64)

def range(start: int, end: int) -> int:
    '''Generate a random integer between start and end, both inclusive.'''
    return int(random() * (end - start + 1)) + start


# Example usage
if __name__ == "__main__":
    print(f"token: {token(8)}")
    print(f"random: {random()}")
    print(f"range(1, 5): {range(1, 5)}")
