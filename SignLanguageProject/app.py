import sys
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.pipeline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()
