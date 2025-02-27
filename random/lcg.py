# Linear Congruential Generator (LCG) randomizer
# Generates random numbers using a Linear Congruential Generator

# X_{n+1} = (aX_n + c) mod m
# Where:
# X_n is the previous random number
# a, c, and m are constants

import time


a = 1664525
c = 1013904223
m = 2**32
global_seed = 18361230
global_state = (global_seed + int(time.time() * 1000)) % m


def seed(s: int):
    '''Set the seed for the random number generator.'''
    global global_state
    global_state = (s + global_seed) % m

def random() -> float:
    '''Returns a random float between 0 and 1 using a Linear Congruential Generator.'''
    global global_state, a, c, m
    global_state = (a * global_state + c) % m
    return global_state / m # Normalize to [0, 1]

def range(start: int, end: int) -> int:
    '''Generate a random integer between start and end, both inclusive.'''
    return int(random() * (end - start + 1)) + start


if __name__ == "__main__":
    print(random())
    