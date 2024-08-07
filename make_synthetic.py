import os 

from src.utility.generate_images import generateImages
import shutil
from distutils.dir_util import copy_tree

def main():
    # remove any existing images in directory
    try:
        shutil.rmtree('data/alzheimer_mri/synthetic')
    except:
        print("directory does not exist")


    # pull real image filepaths and generate a synthetic lookalike
    train_directory = 'data/alzheimer_mri/train'

    for subfolder in os.listdir(train_directory):
        
        destination_directory = train_directory.replace('train','synthetic')+'/'+subfolder
        os.makedirs(destination_directory, exist_ok=True)
        
        if subfolder == 'NonDemented':         
            from_directory = f"{train_directory}/{subfolder}"
            to_directory = f"{destination_directory}/{subfolder}"
            copy_tree(from_directory, to_directory)    
        
        else:
            files = os.listdir(train_directory + '/' + subfolder)
            for f in files:            
                image_path = train_directory + '/' + subfolder + '/' + f
                for r in range(3):
                    generateImages(image_path, destination_directory)

if __name__=='__main__':
    main()