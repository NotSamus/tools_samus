# Steghide Extracter

This is an automatic extracter for steganography. This tool can be used in hackathons, the main benefit is that it is only necessary to input the folder and the program will handle the rest

## Getting Started

In order for this tool to work, it is necessary to have **python** installed and also **steghide**. To install **steghide**, we can use the following command on terminal

```
sudo apt install steghide
```

## How to use it

To use this tool we are going to run the following command:

```
python3 cracker-steg.py
```

the program will ask for a folder, this folder is where you have your images.

The result is something like this:

```
############### EXTRACTING MESSAGES ###############
wrote extracted data to "anime025steg.jpg.txt".
wrote extracted data to "anime017steg.jpeg.txt".
############### START OF ANSWERS ###############
anime025steg.jpg.txt : CAHSI-H4TZ731V
anime017steg.jpg.txt : CAHSI-X3VP695J
```

## How it works

The way this program works is by using the library OS from python, this will help us
to interact with the operating system.

This is going to be the command to extract steganography

```Python
steghide --extract -sf {file} -p "" -xf {file+'.txt'}
```

**Explanation:**

- The flag **-sf** is for the source file, here we have to specify which file we are going to be using to extract the hidden message.
- The flag **-p** goes for the password, in this case all of the files did not have any password so it is reasonable to leave it blank and this will ensure to skip the passwordcheck.
- The flag **-xf** is for how are you going to export the file, in this case we are going to take the same file name we had and just append a _.txt_ this will make a text file.

```Python
 for file in os.listdir():
        os.system(f'steghide --extract -sf {file} -p "" -xf {file+'.txt'}')
```

This will traverse all the files in the folderof images and extract the flag with the name of the file, so its easier to input it in the platform CTF.

## Future improvements

- Implement functionalities for cracking, like to translate from binary to ASCII, etc.
- Implement GUI for easier user use.
