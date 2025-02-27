# Caesar encryption and decryption
# The Caesar cipher is a simple substitution cipher that shifts the alphabet by a fixed number of positions. For example, if the shift is 1, then A becomes B, B becomes C, and so on. The Caesar cipher is named after Julius Caesar, who is said to have used it to communicate with his generals.
# The Caesar cipher is not secure, as there are only 25 possible keys if used with the lowercase English alphabet, as the key 0 is equivalent to the key 26.

import string


def encrypt(alphabet: str, key: int, message: str) -> str:
    '''Encrypt a message using the Caesar cipher (also called: ROT cipher).'''
    result = ""
    for letter in message:
        if letter not in alphabet: # if the letter is not in the alphabet, we don't encrypt it. Alternatively, we could raise an exception.
            result += letter
        else:
            letter_index = alphabet.index(letter)
            total_shift = (letter_index + key) % len(alphabet)
            new_letter = alphabet[total_shift]
            result += new_letter
    return result


def decrypt(alphabet: str, key: int, message) -> str:
    '''Decrypt a message that was encrypted using the Caesar cipher (also called: ROT cipher).'''
    return encrypt(alphabet, -key, message)


assert decrypt(string.ascii_lowercase, 3, encrypt(string.ascii_lowercase, 3, "")) == ""
assert decrypt(string.ascii_lowercase, 1, encrypt(string.ascii_lowercase, 1, "hello")) == "hello"
assert decrypt(string.ascii_lowercase, 5, encrypt(string.ascii_lowercase, 5, "he_llo!")) == "he_llo!"
assert decrypt(string.ascii_lowercase, 55, encrypt(string.ascii_lowercase, 55, "he_llo!")) == "he_llo!"
