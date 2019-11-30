from keras.applications.resnet50 import ResNet50, preprocess_input
from keras.callbacks import ModelCheckpoint
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from resnet152 import ResNet152
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras import Model
import numpy as np

HEIGHT = 300
WIDTH = 300
#base_model = ResNet50(weights='imagenet',include_top =False,input_shape =(HEIGHT, WIDTH, 3))
base_model = ResNet152(weights='imagenet',include_top=False,input_shape=(HEIGHT, WIDTH, 3))

TRAIN_DIR = "dataset"
HEIGHT = 300
WIDTH = 300
BATCH_SIZE = 8

train_datagen = ImageDataGenerator(
      preprocessing_function=preprocess_input,
      rotation_range=90,
      horizontal_flip=True,
      vertical_flip=True
    )

train_generator = train_datagen.flow_from_directory(TRAIN_DIR,
                                                    target_size=(HEIGHT, WIDTH),
                                                    batch_size=BATCH_SIZE)

from keras.layers import Dense, Activation, Flatten, Dropout
from keras.models import Sequential, Model


def build_finetune_model(base_model, dropout, fc_layers, num_classes):
    for layer in base_model.layers:
        layer.trainable = False

    x = base_model.output
    x = Flatten()(x)
    for fc in fc_layers:
        # New FC layer, random init
        x = Dense(fc, activation='relu')(x)
        x = Dropout(dropout)(x)

    # New softmax layer
    predictions = Dense(num_classes, activation='softmax')(x)

    finetune_model = Model(inputs=base_model.input, outputs=predictions)

    return finetune_model


class_list = ["car", "crosswalk", "road", "traficlight"]
FC_LAYERS = [1024, 1024]
dropout = 0.5

finetune_model = build_finetune_model(base_model,
                                      dropout=dropout,
                                      fc_layers=FC_LAYERS,
                                      num_classes=len(class_list))

from keras.optimizers import SGD, Adam

NUM_EPOCHS = 10
BATCH_SIZE = 4
num_train_images = 8

adam = Adam(lr=0.00001)
finetune_model.compile(adam, loss='categorical_crossentropy', metrics=['accuracy'])

filepath="./checkpoints/" + "  ResNet152" + "_model_weights.h5"
checkpoint = ModelCheckpoint(filepath, monitor=["acc"], verbose=1, mode='max')
callbacks_list = [checkpoint]

history = finetune_model.fit_generator(train_generator, epochs=NUM_EPOCHS, workers=8,
                                       steps_per_epoch=num_train_images // BATCH_SIZE,
                                       shuffle=True, callbacks=callbacks_list)

model_json = base_model.to_json()
with open("./model.json", "w") as json_file:
    json_file.write(model_json)

base_model.save_weights("./weights.h5")


img_path = 'car.jpg'
img = image.load_img(img_path, target_size=(300, 300))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = base_model.predict(x)
# decode the results into a list of tuples (class, description, probability)
# (one such list for each sample in the batch)
#print('Predicted:', decode_predictions(preds, top=3)[0])
# Predicted: [(u'n02504013', u'Indian_elephant', 0.82658225), (u'n01871265', u'tusker', 0.1122357), (u'n02504458', u'African_elephant', 0.061040461)]
