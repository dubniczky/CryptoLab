# The Vignere cipher is a polyalphabetic substitution cipher that uses a keyword to shift the alphabet. The keyword is repeated until it matches the length of the message. For example, if the keyword is "key" and the message is "hello", then the keyword is repeated as "keyke" to match the length of the message. The Vignere cipher is more secure than the Caesar cipher, as there are 26 to the power of the message length possible keys if used with the lowercase English alphabet. For 5 letters, that's 26^5 = 11,881,376 possible keys.

import string


def encrypt(alphabet: str, keyword: str, message: str) -> str:
    '''Encrypt a message using the Vignere cipher.'''
    result = ""
    i = 0
    for letter in message:
        if letter not in alphabet:
            result += letter
        else:
            m = alphabet.index(letter)
            k = alphabet.index( keyword[i % len(keyword)] )
            
            total_shift = (m + k) % len(alphabet)
            new_letter = alphabet[total_shift]
            result += new_letter
            i += 1
    return result

def decrypt(alphabet: str, keyword: str, message: str) -> str:
    '''Decrypt a message using the Vignere cipher.'''
    result = ""
    i = 0
    for letter in message:
        if letter not in alphabet:
            result += letter
        else:
            m = alphabet.index(letter)
            k = alphabet.index( keyword[i % len(keyword)] )
            
            total_shift = (m - k) % len(alphabet) # We subtract the shift to decrypt the message
            new_letter = alphabet[total_shift]
            result += new_letter
            i += 1
    return result
    
    
assert decrypt(string.ascii_lowercase, "key", encrypt(string.ascii_lowercase, "key", "")) == ""
assert decrypt(string.ascii_lowercase, "keysm", encrypt(string.ascii_lowercase, "keysm", "hello")) == "hello"
assert decrypt(string.ascii_lowercase, "asd", encrypt(string.ascii_lowercase, "asd", "he_llo!")) == "he_llo!"
assert decrypt(string.ascii_lowercase, "verylongkey", encrypt(string.ascii_lowercase, "verylongkey", "he_llo!")) == "he_llo!"
assert decrypt(string.ascii_lowercase, "key", encrypt(string.ascii_lowercase, "key", "he_llo!")) == "he_llo!"
assert encrypt(string.ascii_lowercase, "key", "oh hi there sir") == encrypt(string.ascii_lowercase, "keykey", "oh hi there sir")
