# Rolling Caesar encryption and decryption
# The rolling Caesar cipher is a variant of the Caesar cipher where the shift is increased by one for each letter. For example, if the shift is 1, then A becomes B, B becomes D, C becomes F, and so on. The rolling Caesar cipher is slightly more secure than the Caesar cipher, as there are 25*25 possible keys if used with the lowercase English alphabet, if we consier the number of rolls part of the key.

import string


def encrypt(alphabet: str, key: int, message: str, roll: int = 1) -> str:
    '''Encrypt a message using the rolling Caesar cipher.'''
    result = ""
    additional = 0
    for letter in message:
        if letter not in alphabet:
            result += letter
        else:
            letter_index = alphabet.index(letter)
            total_shift = (letter_index + key + (additional) * roll) % len(alphabet)
            new_letter = alphabet[total_shift]
            result += new_letter
        additional += 1
    return result


def decrypt(alphabet: str, key: int, message: str, roll: int = 1) -> str:
    '''Decrypt a message that was encrypted using the rolling Caesar cipher.'''
    result = ""
    additional = 0
    for letter in message:
        if letter not in alphabet:
            result += letter
        else:
            letter_index = alphabet.index(letter)
            total_shift = (letter_index - key - (additional) * roll) % len(alphabet)
            new_letter = alphabet[total_shift]
            result += new_letter
        additional += 1
    return result


assert decrypt(string.ascii_lowercase, 3, encrypt(string.ascii_lowercase, 3, "")) == ""
assert decrypt(string.ascii_lowercase, 1, encrypt(string.ascii_lowercase, 1, "hello")) == "hello"
assert decrypt(string.ascii_lowercase, 5, encrypt(string.ascii_lowercase, 5, "he_llo!")) == "he_llo!"
assert decrypt(string.ascii_lowercase, 55, encrypt(string.ascii_lowercase, 55, "he_llo!")) == "he_llo!"
assert decrypt(string.ascii_lowercase, 9, encrypt(string.ascii_lowercase, 9, "he_llo!", roll=3), roll=3) == "he_llo!"
