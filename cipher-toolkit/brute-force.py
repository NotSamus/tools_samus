
import string
"""
Code to bruteforce caesar cipher
"""
alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
"""
This function will make sure to bruteforce the caesar cipher
"""
def caesar_cipher_bruteforce():
    msg = input("Enter the message you would like to decrypt: ").strip()
    for i in range(0,26):
        holder = caesar_cipher(msg, i)
        if 'CAHSI' in holder:
            return holder 
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



def brute_force():
    
    print("Done")


if __name__ == "__main__":
    print(brute_force())