import os 

from src.utility.generate_images import generateImages
import shutil

def main():
    # remove any existing images in directory
    #try:
    #    shutil.rmtree('data/alzheimer_mri/synthetic')
    #except:
    #    print("directory does not exist")

    # pull real image filepaths and generate a synthetic lookalike
train_directory = 'data/alzheimer_mri/train'

for subfolder in os.listdir(train_directory):
    
    destination_directory = train_directory.replace('train','synthetic')+'/'+subfolder

    #os.makedirs(destination_directory, exist_ok=True)
    
    files = [
        f for f in os.listdir(train_directory + '/' + subfolder)
        if int(f.split("_")[1].split(".")[0]) not in [
            int(f.split("_")[1]) for f in os.listdir(destination_directory)
            ]
        ]
    for f in files:
        image_path = train_directory + '/' + subfolder + '/' + f
        for r in range(3):
            generateImages(image_path, destination_directory)
        print(f)

if __name__=='__main__':
    main()