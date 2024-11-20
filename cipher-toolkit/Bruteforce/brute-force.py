import re

"""
Code to bruteforce caesar cipher
"""
alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
"""
This function will make sure to bruteforce the caesar cipher
"""
def caesar_cipher_bruteforce(msg):
    msg = msg.strip()
    for i in range(0,26):
        holder = caesar_cipher(msg, i)
        if 'CAHSI' in holder:
            return f'Key: {i}\nMessage: {holder}' 
"""
This is the algorithm of caesar cipher
"""
def caesar_cipher(msg,key):
    plaintext = ""
    for char in msg:
        if char.isalpha():  # Check if the character is a letter
            shift = 65 if char.isupper() else 97  # Determine ASCII base for uppercase/lowercase
            # Perform the shift (wrapping around with modulo)
            decrypted_char = chr((ord(char) - shift - key) % 26 + shift)
            plaintext += decrypted_char
        else:
            # Non-alphabetic characters are added unchanged
            plaintext += char
    return plaintext

# This might be to implement the cipher from binary to hex and viceversa
def identifier(s):
    # This is for binary
    if(bool(re.fullmatch(r'[01]+', s))):
        return 'binary'
    elif bool(re.fullmatch(r'([0-9A-Fa-f]{2}\s*)+', s)):
        return 'hex'
    # This is for Base64
    elif(bool(re.fullmatch(r'.*=$', s))):
        return 'base64'
    # elif all(33 <= ord(c) <= 126 for c in s):
    elif bool(re.fullmatch(r'^[!-~]+$',s)):
        return 'rot47'
    else:
        return 'unknown'



def brute_force():
    user = input("Enter the cipher to crack:\n>")
    # identifier(user)
    caesar_cipher_bruteforce(user)
    print("Done")


if __name__ == "__main__":
    brute_force()