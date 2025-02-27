import math
import time

# The base seed is always added to the seed that is set randommly or by the user to provide additional randomness.
base_seed = 1976123.5081254
# A static number that is generated based on the time when the program is run.
# This is weak to timing attacks, so never use it for secure random number generation.
global_seed = base_seed + int(time.time() * 1000)
global_step = 0


def seed(s: int):
    '''Set the seed for the random number generator.'''
    global global_seed
    global_seed = base_seed + s

def random() -> float:
    '''Returns a random float between 0 and 1 using the fractional part of the sine function.'''
    global global_seed, global_step
    global_step += 1
    num = (math.sin(global_seed + global_step)+1) * 43659.98891672314
    return num - int(num) # Return the fractional part of the number

def range(start: int, end: int) -> int:
    '''Generate a random integer between start and end, both inclusive.'''
    return int(random() * (end - start + 1)) + start


if __name__ == "__main__":
    seed(123)
    print(random())
    print(range(1,2))
    print(range(1,2))
