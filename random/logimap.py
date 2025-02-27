# Random number generator using the logistic map.
# The logistic map is a chaotic map that is defined by the equation:
# X_{n+1} = r * X_n * (1 - X_n)

import time


global_seed = 0.5
global_r = 3.5 + (int(time.time() * 1000) / 1000) % 0.5 # The r value is set to 3.5 + the fractional part of the current time


def random() -> float:
    '''Returns a random float between 0 and 1 using the logistic map.'''
    global global_seed, global_r
    global_seed = global_r * global_seed * (1 - global_seed)
    return global_seed

def range(start: int, end: int) -> int:
    '''Generate a random integer between start and end, both inclusive.'''
    return int(random() * (end - start + 1)) + start


if __name__ == "__main__":
    print(random(), random(), random())