import os
import sys
import numpy as np
import pandas as pd


##common constant variable for training pipeline
TARGET_COLUMN="Result"
PIPELINE_NAME: str="NworkSecurity"
ARTIFACT_DIR: str="Artifacts"
FILE_NAME: str="phisingData.csv"

TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str ="test.csv"


##data ingestion related constants
DATA_INGESTION_COLLECTION_NAME: str="NetworData"
DATA_INGESTION_DATABASE_NAME: str="AKSHITA"
DATA_INGESTION_DIR_NAME: str="data_ingestion"
DATA_INGESTION_FEATURE_STROE_DIR: str="feature_store"
DATA_INGESTION_INGESTED_DIR: str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION :float=0.2