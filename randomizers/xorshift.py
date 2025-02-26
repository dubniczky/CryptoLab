# Randomly shifts bits of a seed to generate a random number
# Not a cryptographically secure random number generator, but it is very fast.

import time


global_seed = 18361230
global_state = (global_seed + int(time.time() * 1000)) & 0xFFFFFFFF


def seed(s: int):
    '''Set the seed for the random number generator.'''
    global global_state
    global_state = (s + global_seed) & 0xFFFFFFFF

def random():
    '''Returns a random float between 0 and 1 using a XOR operations and bitshifts.'''
    global global_state
    global_state ^= (global_state << 13) & 0xFFFFFFFF
    global_state ^= (global_state >> 17) & 0xFFFFFFFF
    global_state ^= (global_state << 5) & 0xFFFFFFFF
    return global_state / 0xFFFFFFFF

def range(start: int, end: int) -> int:
    '''Generate a random integer between start and end, both inclusive.'''
    return int(random() * (end - start + 1)) + start


if __name__ == "__main__":
    print(random())
