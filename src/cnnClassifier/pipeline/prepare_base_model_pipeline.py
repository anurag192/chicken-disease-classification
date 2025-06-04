import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.cnnClassifier.entity.config_entity import PrepareBaseModelConfig
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.prepare_base_model import PrepareBaseModel
from src.cnnClassifier import logger

STAGE_NAME="Prepare Base Model"

class PrepareBaseModelPipeline:
    def __init__(self):
        pass

    def prepare_base_model(self):
        try:
            config=ConfigurationManager()
            prepare_base_model_config=config.get_prepare_base_model()
            prepare_base_model=PrepareBaseModel(prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()

        except Exception as e:
            raise e

if __name__=="__main__":
    try:
        logger.info(f"{STAGE_NAME} started")
        obj=PrepareBaseModelPipeline()
        obj.prepare_base_model()
        logger.info(f"{STAGE_NAME} completed")

    except Exception as e:
        raise e


