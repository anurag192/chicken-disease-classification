from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

from src.cnnClassifier.pipeline.prepare_base_model_pipeline import PrepareBaseModelPipeline

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
    

