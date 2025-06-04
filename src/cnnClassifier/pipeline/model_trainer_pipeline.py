import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.pipeline.prepare_callback import PrepareCallback
from src.cnnClassifier.components.model_trainer import Training
from src.cnnClassifier import logger
STAGE_NAME="Training"

class ModelTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
            
            config=ConfigurationManager()
            prepare_callback_config=config.get_prepare_callback()
            prepare_callback=PrepareCallback(prepare_callback_config)
            callback_list=prepare_callback.get_tb_callback

            training_config=config.get_training_config()
            training=Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train(callback_list=callback_list)


if __name__=="__main__":
    try:
          logger.info(f"{STAGE_NAME} started")
          obj=ModelTrainingPipeline()
          obj.main()
          logger.info(f"{STAGE_NAME} ended")

    except Exception as e:
         logger.exception(e)
         raise e

    


