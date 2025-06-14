import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
import tensorflow as tf

from typing import List
from src.cnnClassifier.entity.config_entity import ModelTrainerConfig
from pathlib import Path

class Training:
    
    def __init__(self,config:ModelTrainerConfig):
        self.config=config

    def get_base_model(self):
        self.model=tf.keras.models.load_model(
            self.config.updated_base_model,
            compile=False

        )
        self.model.compile(
        optimizer=tf.keras.optimizers.SGD(learning_rate=self.config.params_learning_rate),
        loss=tf.keras.losses.CategoricalCrossentropy(),
        metrics=["accuracy"]
        )

    def train_valid_generator(self):
        datagenerator_kwargs=dict(
            rescale=1/255.0,
            validation_split=0.2
        )

        dataflow_kwargs=dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation='bilinear'
        )
        valid_datagenerator=tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )
        self.valid_generator=valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            train_datagenerator=tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                shear_range=0.2,
                zoom_range=0.2,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                **datagenerator_kwargs
                
            )

        else:
            train_datagenerator=valid_datagenerator

        self.train_generator=train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs

            
        )

    @staticmethod
    def save_model(model:tf.keras.Model,path:Path):
        model.save(path)


    def train(self,callback_list:List):
        self.steps_per_epoch=self.train_generator.samples//self.train_generator.batch_size
        self.validation_steps=self.valid_generator.samples//self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator,
            callbacks=callback_list

        )
        self.save_model(
            path=self.config.trained_model_file_path,
            model=self.model
        )

        