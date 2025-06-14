from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir:Path
    source_URL:str
    local_data_file:Path
    unzip_dir:Path


@dataclass
class PrepareBaseModelConfig:
    root_dir:Path
    base_model_path:Path
    updated_base_model_path:Path
    params_image_size:list
    params_learning_rate:float
    params_include_top:bool
    params_weight:str
    params_classes:int


@dataclass(frozen=True)
class PrepareCallbackConfig:
    root_dir:Path
    tensorboard_root_log_dir:Path
    checkpoint_model_file_path:Path


@dataclass
class ModelTrainerConfig:
    root_dir:Path
    trained_model_file_path:Path
    updated_base_model:Path
    training_data:Path
    params_epochs:int
    params_batch_size:int
    params_is_augmentation:bool
    params_image_size:int
    params_learning_rate:int


@dataclass
class EvaluationConfig:
    path_of_model:Path
    training_data:Path
    all_params:dict
    params_image_size:list
    params_batch_size:int


    