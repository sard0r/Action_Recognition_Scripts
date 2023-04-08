import os 
from glob import glob
import shutil
import json
from tqdm import tqdm

needless_path = []
path = "E:/label_data"

for i in tqdm(os.listdir(path), desc='Processing folders', unit='folder'):
    new_path = os.path.join(path, i)
    json_files = glob(f'{new_path}/*.json')
    for jsons in json_files:
        dir_path, file_name = os.path.split(jsons)
        # Replace the file extension from .json to .jpg
        new_file_name = file_name.replace('.json', '.jpg')
        # Create the new file path with the updated file extension
        image = os.path.join(dir_path, new_file_name)
        with open(jsons, 'r') as file:
            data = json.load(file)
            if len(data['content']['object']['annotation']['bboxes'])==0:
                needless_path.append(image)
                needless_path.append(jsons)

for i in tqdm(needless_path, desc='Deleting needless files', unit='file'):
    os.remove(i)