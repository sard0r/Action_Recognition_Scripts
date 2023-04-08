import os 
from glob import glob
from tqdm import tqdm

path = 'E:/label_data'
folders = os.listdir(path)
for folder in tqdm((folders), desc='remove json files'):
    folder_path = os.path.join(path, folder)
    json_files = glob(os.path.join(folder_path, '*.json'))
    for json_file in json_files:
        os.remove(json_file)