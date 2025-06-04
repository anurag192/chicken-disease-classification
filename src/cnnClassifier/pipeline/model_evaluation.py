import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.entity.config_entity import (EvaluationConfig)
from src.cnnClassifier.components.model_evaluation import Evaluation
from src.cnnClassifier import logger


STAGE_NAME="Model Evaluation"

class EvaluationPipeline:

    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        validation_config=config.get_validation_config()
        evaluation=Evaluation(validation_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__=="__main__":
    try:
        logger.info(f"{STAGE_NAME} started")
        obj=EvaluationPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} ended")

    except Exception as e:
        raise e