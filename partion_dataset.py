
import os
from glob import glob
import shutil
from sklearn.model_selection import train_test_split

#getting list of images
image_files = glob("train/*.png")

#replacing the extension
images = [name.replace(".png","") for name in image_files]

#splitting the dataset
train_names, test_names = train_test_split(images, test_size=0.2)

def batch_move_files(file_list, source_path, destination_path):
    for file in file_list:
        #extracting only the name of the file and concatenating with extenions
        image = file.split('\\')[1] + '.png'
        xml = file.split('\\')[1] + '.xml'
        shutil.move(os.path.join(source_path, image), destination_path)
        shutil.move(os.path.join(source_path, xml), destination_path)
    return

source_dir = "train"
test_dir = "dataset_hanhvi/test/"
train_dir = "dataset_hanhvi/train/"
batch_move_files(train_names, source_dir, train_dir)
batch_move_files(test_names, source_dir, test_dir)