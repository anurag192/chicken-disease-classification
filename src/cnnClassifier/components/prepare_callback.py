import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from src.cnnClassifier.entity.config_entity import PrepareCallbackConfig

class PrepareCallback:

    def __init__(self,config:PrepareCallbackConfig):
        self.config=config

    @property
    def create_tb_callbacks(self):
        timestamp=time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir=os.path.join(self.config.tensorboard_root_log_dir,
                                        f"tb_logs_at_{timestamp}")
        
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    
    @property
    def create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_file_path,
            save_best_only=True
        )
    
    @property

    def get_tb_callback(self):
        return [
            self.create_tb_callbacks,
            self.create_ckpt_callbacks
        ]
