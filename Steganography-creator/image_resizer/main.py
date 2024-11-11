from PIL import Image
import shutil
import os
def resize(image_path,filename, path):
    
    with Image.open(image_path) as img:
        # Change size as needed 
        new_width = 300
        new_height = 200
        
        img_r = img.resize((new_width, new_height))
        img_r.save(f'{path}/n_{filename}')    
        os.system(f'rm {image_path}')

def main():
    dir = '/Users/lopez/projects/scrap-code/useful_tools/image_resizer/renamed_pictures'
    dir_2 = '/Users/lopez/projects/scrap-code/useful_tools/image_resizer/resized_pictures'
    
    if os.path.isdir('resized_pictures'):
        os.system('rm -rf resized_pictures')
        shutil.copytree(dir, dir_2)
    else:
        shutil.copytree(dir, dir_2)
        
    for filename in os.listdir(dir_2):
        file_path = os.path.join(dir_2, filename)
        if os.path.isfile(file_path):
            resize(file_path,filename,dir_2)
    print('done')

if __name__ == '__main__':
    main()