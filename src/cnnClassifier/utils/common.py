import joblib
from ensure import ensure_annotations
import json
from pathlib import Path
from typing import Any
import os
import yaml
from box import ConfigBox
from src.cnnClassifier import logger
from box.exceptions import BoxValueError
import base64

@ensure_annotations

def read_yaml(path_to_yaml:Path)->ConfigBox:

    with open(path_to_yaml,'r') as yaml_file:
        try:
            content=yaml.safe_load(yaml_file)
            logger.info(f"{path_to_yaml} loaded successfully")
            return ConfigBox(content)
        except BoxValueError:
            raise ValueError("yaml file is empty")

@ensure_annotations

def create_directories(path_to_directories:list,verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)

        if verbose:
            logger.info(f"Created directory {path}")

@ensure_annotations

def save_json(path:Path,data:dict):

    with open(path,'w') as f:
        json.dump(data,f,indent=4)

    logger.info(f"JSON file saved at {path}")

@ensure_annotations

def load_json(path:Path)->ConfigBox:

    with open(path,'r') as f:
        content=json.load(f)

    logger.info(f"JSON loaded successfully")
    return ConfigBox(content)

@ensure_annotations

def save_bin(data:Any,path:Path):
    with open(path,'w') as f:
        joblib.dump(data,f)

    logger.info("Model loaded")

@ensure_annotations

def load_bin(data:Any,path:Path):
    with open(path,'r') as f:
        content=json.load(f)

    return content

@ensure_annotations

def get_size(path:Path)->str:

    size_in_kb=round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"

def decodeimage(imgstring,filename):
    imgdata=base64.b64decode(imgstring)

    with open(filename,'wb') as f:
        f.write(imgdata)
        f.close()

def encodeimage(croppedImagePath):
    with open(croppedImagePath,'rb') as f:
        return base64.b64encode(f.read())







    


