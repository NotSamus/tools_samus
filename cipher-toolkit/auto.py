import re
import base64


"""class helper
This class is for the helper functions for the automatic toolkit.a

"""
class helper:
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
    def is_binary_string(s):
        return True;
    
if __name__ == "__main__":
    a = input('\n>')
    print(helper.identifier(a))
    print('happy cracking!')