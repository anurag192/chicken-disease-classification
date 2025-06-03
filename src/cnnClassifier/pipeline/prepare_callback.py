import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from src.cnnClassifier.entity.config_entity import PrepareCallbackConfig
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.prepare_callback import PrepareCallback

STAGE_NAME="Prepare Callback Pipeline"

class PrepareCallbackPipeline:
    def __init__(self):
        pass

    def prepare_callback(self):
        try:
            config=ConfigurationManager()
            prepare_callback_config=config.get_prepare_callback()
            prepare_callback=PrepareCallback(prepare_callback_config)
            callback_list=prepare_callback.get_tb_callback

        except Exception as e:
            raise e

