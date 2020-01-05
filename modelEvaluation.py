import os
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from keras.applications.resnet50 import preprocess_input
from keras_preprocessing.image import ImageDataGenerator
from keras.applications.resnet50 import ResNet50, preprocess_input
from keras.callbacks import ModelCheckpoint
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from resnet152 import ResNet152
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras import Model, metrics
from tensorflow import keras
from datetime import datetime
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from keras import *
TEST_DIR = "dataset/testing"
Two_Classes = ['damage','whole']
HEIGHT = 300
WIDTH = 300
modelPath = "./checkpoints/" + "Two_Classes" + "/" + "ResNet50_model.h5"
checkpoint = ModelCheckpoint(modelPath, monitor=["acc"], verbose=1, mode='max')
callbacks_list = [checkpoint]
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, modelPath)
if os.path.exists(my_file):
    print('Model named ' + "Two_Classes" + ' Successfully loaded')
    finetune_model = tf.keras.models.load_model(modelPath)
else:
    errorString = ("No model or path found, check ")
    model = load_model(my_file)
    print("No model found to load, please check your 'checkpoints' directory")
    exit()
#Creating a timestamp in order to sort the plot results
now = datetime.now()
TimeString = ""
timestamp = datetime.timestamp(now)
DateTime_object = datetime.fromtimestamp(int(timestamp))
TimeString = DateTime_object.strftime("Date - %Y-%m-%d Time - %X") #Formatted string
Stamp = TimeString.replace(":","_")
file_count = os.listdir("./dataset/testing/damage") + os.listdir("./dataset/testing/whole")
num_test_images = len(file_count)
TRAIN_BATCH_SIZE = int(num_test_images // 10)
test_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    rotation_range=90,
    horizontal_flip=True,
    vertical_flip=True,)
test_generator = test_datagen.flow_from_directory(TEST_DIR,
                                                    target_size=(HEIGHT, WIDTH),
                                                    batch_size=TRAIN_BATCH_SIZE,
                                                    class_mode='categorical',
                                                    shuffle=True)
eval_Result = finetune_model.evaluate_generator(test_generator, workers=8, verbose=1)
print("\n%s: %.4f , %s: %.2f%%" %(finetune_model.metrics_names[0], eval_Result[0], finetune_model.metrics_names[2], eval_Result[2]*100))
# list all data in history for current training, both loss and accuracy compared between the training and validation sets. also save the tables locally.
