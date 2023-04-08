import os 
from glob import glob
import json


def convert_centernet_to_yolov5(centernet_annotations, output_folder):
    with open(centernet_annotations) as file:
        json_data = json.load(file)
        file_name = json_data['image']['file_name'].split('.')
        file_name_without_extension = ".".join(file_name[:-1])
        file_name_with_extension = file_name_without_extension + ".txt"
        bboxes = json_data['content']['object']['annotation']['bboxes']
        output_path = os.path.join(output_folder, file_name_with_extension)
        with open(output_path, 'w') as yolov5_file:
            for bbox in bboxes:
                x_center = (bbox[0]+bbox[2])/2
                y_center = (bbox[1]+bbox[3])/2
                width = bbox[2]-bbox[0]
                height = bbox[3]-bbox[1]
                yolov5_file.write(f"{0} {x_center} {y_center} {width} {height}\n")

path = 'E:/label_data'
folders = os.listdir(path)
for folder in folders:
    folder_path = os.path.join(path, folder)
    json_files = glob(os.path.join(folder_path, '*.json'))
    for json_file in json_files:
        convert_centernet_to_yolov5(json_file, folder_path)

