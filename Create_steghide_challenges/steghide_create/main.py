import os

def reader():
    print(os.getcwd())
    i=1
    for filename in os.listdir('steg_pictures'):
        os.system(f'steghide embed -cf steg_pictures/n_cat_{i}.jpg -ef flags_separated/secret_{i}.txt -p "" ' )
        i+=1
            
def flag_separator():
    if os.path.isdir('flags_separated'):
        os.system('rm -rf flags_separated')
        os.mkdir('flags_separated')
    else:
        os.mkdir('flags_separated')
    with open("Flags.txt",'r') as file:
        i=1
        for line in file:
            path=f'flags_separated/secret_{i}.txt'
            with open(path, 'w') as file:
                file.write(f"{line}")
                print(f"{path}")
                i+=1
            
def main():
    # directory = "/Users/lopez/projects/scrap-code/useful_tools/steghide_create/"
    flag_separator() #This is to separate the files from the flag file
    reader()
if __name__ == "__main__":
    main()