import os
import shutil
def renamer(dir):
    i = 1
    for filename in os.listdir(dir):
        if filename.endswith('.JPG'):
            old = os.path.join(dir, filename)
            new = os.path.join(dir, f'cat_{i}.jpg')
            os.rename(old, new)
            i +=1
    print('done')
    
def main():
    dir = '/Users/lopez/projects/scrap-code/useful_tools/image_renamer/pictures'
    dir_2 = '/Users/lopez/projects/scrap-code/useful_tools/image_renamer/renamed_pictures'
    
    if os.path.isdir('renamed_pictures'):
        os.system('rm -rf renamed_pictures')
        shutil.copytree(dir, dir_2)
    else:
        shutil.copytree(dir, dir_2)

    renamer(dir_2)

if __name__ == '__main__':
    main()
