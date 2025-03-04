# Simple monoalphabetic substitution cipher

import random
import string


def _randomize_alphabet(alphabet: str) -> str:
    alphabet = list(alphabet)
    random.shuffle(alphabet)
    return ''.join(alphabet)

def encrypt(table: tuple[str, str], message: str) -> str:
    m = table[0]
    c = table[1]
    cipher = ''
    for char in message:
        if char in m:
            cipher += c[m.index(char)]
        else:
            cipher += char
    return cipher

def decrypt(table: tuple[str, str], ciphertext: str) -> str:
    return encrypt((table[1], table[0]), ciphertext)



assert (alphabet := _randomize_alphabet(string.ascii_letters)) != string.ascii_letters
assert decrypt((string.ascii_letters, alphabet), encrypt((string.ascii_letters, alphabet), 'Hello')) == 'Hello'
assert decrypt((string.ascii_letters, alphabet), encrypt((string.ascii_letters, alphabet), 'ahoy!')) == 'ahoy!'
