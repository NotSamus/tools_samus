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
        inp = input('Eneter Base64 String:\n> ')
        try:
            decoded=base64.b64decode(inp).decode('utf-8')
            print('')
            print('Decoded String:',decoded)
        except Exception as e:
            print('Error decoding Base64:',e)
    @staticmethod
    def B32():
        inp = input('Enter Base32 String:\n> ')
        try:
            decoded = base64.b32decode(inp).decode('utf-8')
            print('')
            print('Decoded String:',decoded)
        except Exception as e:
            print('Error decoding Base32:',e)
    @staticmethod
    def BinaryToText():
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
    toolkit.main()