"""_summary_
main.py

This is a class that provides a toolkit for decoding some ciphers that are used in hackathons and CTFs.
The toolkit provides the following options:
    a. Base64 Decoder
    b. Base32 Decoder
    c. Binary to text
    
It runs in the commandline.
"""

import base64
import re

class craker:
    def main(s):
        # while not('CAHSI'in s):            
            if(helper.is_binary_string('01010101')):
                toolkit.BinaryToText()
            print('Happy cracking!')

class helper:
    def identifier(s):
        # This is for binary
        if(bool(re.fullmatch(r'[01]*', s))):
            return 'binary'
        # This is for Base64
        elif(bool(re.fullmatch(r'.*=$', s))):
            return 'base64'
        elif all(33 <= ord(c) <= 126 for c in s):
            return 'rot47'
        elif re.fullmatch(r'^[A-Za-z]+$', s):
            return 'rot13'
        else:
            return 'unknown'
    def is_binary_string(s):
        return True;

class toolkit:
    @staticmethod
    def main():
        while True:
            print('##########################')
            print('### Welcome to Toolkit ###')
            print('##########################')
            print('Option:')
            print('a. Base64 Decoder')
            print('b. Base32 Decoder')
            print('c. Binary to text')
            user = input('Please choose an option:\n> ')

            switch_dict = {
                'a': toolkit.B64,
                'b': toolkit.B32,
                'c': toolkit.BinaryToText,
                'e': toolkit.exit_toolkit
            }
            func = switch_dict.get(user, lambda: print("Invalid option"))
            func()
    @staticmethod
    def B64():
        """
        Base 64 decoder
        
        Asks the user for the Base64 String and decodes it.
        
        Raises:
            Exception: if there was an error when decoding a base64 string.
        """
        inp = input('Eneter Base64 String:\n> ')
        try:
            decoded=base64.b64decode(inp).decode('utf-8')
            print('')
            print('Decoded String:',decoded)
        except Exception as e:
            print('Error decoding Base64:',e)
    @staticmethod
    def B32():
        """
        Base 32 decoder
        
        Asks the user for the Base32 String and decodes it.
        
        Raises:
            Exception: if there was an error when decoding a base32 string.
        """
        inp = input('Enter Base32 String:\n> ')
        try:
            decoded = base64.b32decode(inp).decode('utf-8')
            print('')
            print('Decoded String:',decoded)
        except Exception as e:
            print('Error decoding Base32:',e)
    @staticmethod
    def BinaryToText():
        """
        Binary to text decoder
        
        Asks the user for the Binary String and decodes it.
        
        """
        inp = input('Enter Binary String:\n> ')
        inp = inp.split()
        collection = [chr(int(i, 2)) for i in inp]
        print('')
        print(''.join(collection))

    @staticmethod
    def exit_toolkit():
        print('Byeee, Happy hacking!')
        exit()

if __name__ == "__main__":
    # toolkit.main()
    # craker.main()
    print(helper.identifier('uryyb'))