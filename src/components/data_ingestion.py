import os
import sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#from src.components.data_transformation import DataTransformation
#from src.components.model_trainer import ModelTrainerConfig
#from src.components.model_trainer import ModelTrainer

import pickle
import random
import cv2
import numpy as np


class DataIngestionConfig:
    # This creates a file path for train.csv, test.csv and data.csv inside the artifacts folder.
    features =os.path.join("artifacts","X.pickle")
    lables =os.path.join('artifacts',"Y.pickle")


@dataclass
class DataIngestion:
    #The __init__() method is a constructor.
    #It runs automatically whenever an object of the class is created.
    def __init__(self):
        #This creates an object of the DataIngestionConfig class and stores it inside the current DataIngestion object.
        #So now the DataIngestion class can access all file paths from DataIngestionConfig.
        self.ingestion_config = DataIngestionConfig()


    def initiate_data_ingestion(self):
        logging.info("Enter the data ingestion method or component")

        DATA_DIR = "notebook/malimg_paper_dataset_imgs"

        CATEGORIES = ["Adialer.C", "Agent.FYI", "Allaple.A", "Allaple.L", "Alueron.gen!J", "Autorun.K", "BenginPe", "C2LOP.gen!g", "C2LOP.P", "Dialplatform.B", "Dontovo.A", "Fakerean", "Instantaccess", "Lolyda.AA1", "Lolyda.AA2", "Lolyda.AA3", "Lolyda.AT", "Malex.gen!J", "Obfuscator.AD", "Rbot!gen", "Skintrim.N", "Swizzor.gen!E", "Swizzor.gen!I", "VB.AT", "Wintrim.BX", "Yuner.A"]

        IMG_SIZE = 64

        training_data = []

        try:
            logging.info('Read images from lables and features from dataset folder')
            for category in CATEGORIES:
                path = os.path.join(DATA_DIR, category)
                class_num = CATEGORIES.index(category)
                for img in os.listdir(path):
                    try:
                        
                        img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
                        new_array = cv2.resize(img_array,( IMG_SIZE, IMG_SIZE))
                        
                        training_data.append([new_array,class_num])
                    
                    except Exception as e:
                        raise CustomException (e,sys)
                
                print(CATEGORIES[class_num])


            #read the data.csv.
            #change this line out if you want to read the data from other sourses ex: database, api, etc
            #df=pd.read_csv('notebook/data/stud.csv')
            #loggs it
            os.makedirs(os.path.dirname(self.ingestion_config.features), exist_ok = True)

            random.shuffle(training_data)
            X = []
            Y = []

            for features, label in training_data:
                X.append(features)
                Y.append(label)

            X = np.array(X).reshape(-1,IMG_SIZE,IMG_SIZE,1)

            pickle_out = open("artifacts/X.pickle", "wb")
            pickle.dump( X, pickle_out)
            pickle_out.close()

            pickle_out = open("artifacts/Y.pickle", "wb")
            pickle.dump( Y, pickle_out)
            pickle_out.close()




            logging.info("Ingestion of data is completed")

            return (
                #data_transformation.py will grab the return values and the datapoints and start the process
                self.ingestion_config.features,
                self.ingestion_config.lables
            )

        except Exception as e:
            raise CustomException (e,sys)
        
if __name__=='__main__':
    obj=DataIngestion()
        #old test
    obj.initiate_data_ingestion()