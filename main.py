from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

from src.cnnClassifier.pipeline.prepare_base_model_pipeline import PrepareBaseModelPipeline
from src.cnnClassifier.pipeline.prepare_callback import PrepareCallbackPipeline
from src.cnnClassifier.pipeline.model_trainer_pipeline import ModelTrainingPipeline
from src.cnnClassifier.pipeline.model_evaluation import EvaluationPipeline

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f"{STAGE_NAME} started")
    obj=DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME} completed")

except Exception as e:
    raise e


STAGE_NAME="Prepare Base Model Pipeline"
try:
        logger.info(f"{STAGE_NAME} started")
        obj=PrepareBaseModelPipeline()
        obj.prepare_base_model()
        logger.info(f"{STAGE_NAME} completed")

except Exception as e:
     raise e
    
STAGE_NAME="Prepare Callback Pipeline"
try:
     logger.info(f"{STAGE_NAME} started")
     obj=PrepareCallbackPipeline()
     obj.prepare_callback()
     logger.info(f"{STAGE_NAME} completed")

except Exception as e:
     raise e


STAGE_NAME="Model Trainer Pipeline"

try:
     logger.info(f"{STAGE_NAME} started")
     obj=ModelTrainingPipeline()
     obj.main()
     logger.info(f"{STAGE_NAME} completed")

except Exception as e:
     raise e

STAGE_NAME="Model Evaluation Pipeline"
try:
     logger.info(f"{STAGE_NAME} started")
     obj=EvaluationPipeline()
     obj.main()
     logger.info(f"{STAGE_NAME} ended")

except Exception as e:
     raise e



