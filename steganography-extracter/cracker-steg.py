#!/usr/bin/env python3

import os

def crack(steg_folder):
    os.chdir(steg_folder)
    print('############### EXTRACTING MESSAGES ###############')
    for file in os.listdir():
        print(file)
        os.system(f'steghide --extract -sf {file} -p "" -xf {file+'.txt'}')
        # print(f'steghide --extract -sf {file} -p "" -xf {file+'.txt'}')
    print('############### START OF ANSWERS ###############')    
    for filea in os.listdir():
        if filea.endswith('.txt'):
            with open(filea,'r') as f1:
                content = f1.read()
                print(f'{filea}:{content}')
    
def main():
    # Ask for the folder to crack
    folder = input("Folder name:")
    print()
    print()
    
    # call the program
    crack(folder)
   
    print('Happy Hacking')


if __name__ == "__main__":
    main()