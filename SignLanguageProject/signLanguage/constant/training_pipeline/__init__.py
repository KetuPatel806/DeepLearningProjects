import os

ARTIFACTS_DIR: str = "artifacts"

""""
Data Ingestion related constant start with DATA_INGESTION_VAR_NAME
"""

## This constant used for the Data Ingestion Directory
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
## This constant used for the Feature Storing Directory
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
## This constant used for the Ingested Data Directory/Data Download Directory
DATA_DOWNLOAD_URL: str = "https://github.com/entbappy/Branching-tutorial/raw/master/Sign_language_data.zip"

""""
Data Validation related constant start with DATA_VALIDATION_VAR_NAME
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = "status.txt"

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "test" ,"data.yaml"]


""""
MODEL TRAINER related constant start with MODEL_TRAINER_VAR_NAME
"""

MODEL_TRAINER_DIR_NAME = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME = "yolov5s.pt"

MODEL_TRAINER_BATCH_SIZE = 16

MODEL_TRAINER_NUM_EPOCHS = 5

""""
MODEL PUSHER related constant start with MODEL_PUSHER_VAR_NAME
"""
BUCKET_NAME = "sign-language-bucket-s3"
S3_MODEL_NAME = "best.pt"