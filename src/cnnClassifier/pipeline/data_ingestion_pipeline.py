from src.cnnClassifier.entity.config_entity import DataIngestionConfig
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.data_ingestion import DataIngestion

from src.cnnClassifier import logger

STAGE_NAME="Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        try:
            config=ConfigurationManager()
            data_ingestion_config=config.get_data_ingestion_config()
            data_ingestion=DataIngestion(data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip()

        except Exception as e:
            raise e
        
if __name__=="__main__":
    try:
        logger.info(f"{STAGE_NAME} started")
        obj=DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f"{STAGE_NAME} completed")

    except Exception as e:
        raise e