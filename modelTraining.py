def modelTrainer(modelType):
    from keras.applications.resnet50 import ResNet50, preprocess_input
    from keras.callbacks import ModelCheckpoint
    from keras.preprocessing.image import ImageDataGenerator
    from keras.preprocessing import image
    from resnet152 import ResNet152
    from keras.applications.resnet50 import preprocess_input, decode_predictions
    from keras import Model, metrics
    from tensorflow import keras
    import numpy as np
    import tensorflow as tf
    import matplotlib.pyplot as plt
    from datetime import datetime
    import time
    import os
    from keras.optimizers import SGD, Adam
    from keras.utils import plot_model

    #General variables for GUI interaction and choices :
    Two_Classes = ['damage','whole']
    Three_Classes = ['front','rear','side']
    '''
    Class_List_From_Gui = Two_Classes
    runIdentifier = -1
    Epocs_from_Gui = -1
    learningRate_From_Gui = -1
    regularizationRate_From_Gui = -1
    numTrain_From_Gui = -1
    numVal_From_Gui = -1
    Train_BatchSize_From_Gui = -1
    Val_BatchSize_From_Gui = -1
    Graph_Naming = -1
    '''
    #Using the configuration file, we initiate our variables as the user defined,
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, "./Init.ini")
    with open(my_file,"r") as fp:
        line = fp.readline()
        while line:
            LineCleaner = line.split("=")
            temp = LineCleaner[1][:-1]
            LineCleaner[1] = temp
            #Python has no Switch-case, so we use ifelse statements:
            if LineCleaner[0] == "New_Model" :
                if LineCleaner[1] == "New" :
                    Train_new = True
                elif LineCleaner[1] == "Old" :
                    Train_new = False
            if LineCleaner[0] == 'Class_List_From_Gui':
                if LineCleaner[1] == 'Two_Classes':
                    class_list = Two_Classes
                else:
                    class_list = Three_Classes
            elif LineCleaner[0] == 'Epocs_from_Gui':
                if LineCleaner[1] == '-1':
                    NUM_EPOCHS = 20 #default
                else:
                    NUM_EPOCHS = int(LineCleaner[1])
            elif LineCleaner[0] == 'learningRate_From_Gui':
                if LineCleaner[1] == '-1':
                    LR_Adam = 0.0001
                else:
                    LR_Adam = float(LineCleaner[1])
            elif LineCleaner[0] == 'regularizationRate_From_Gui':
                if LineCleaner[1] == '-1':
                    l1_Reg = 0.005
                else:
                    l1_Reg = float(LineCleaner[1])
            elif LineCleaner[0] == 'numTrain_From_Gui':
                if LineCleaner[1] == '-1':
                    num_train_images = 1840
                else:
                    num_train_images = int(LineCleaner[1])
            elif LineCleaner[0] == 'numVal_From_Gui':
                if LineCleaner[1] == '-1':
                    num_val_images = 480
                else:
                    num_val_images = int(LineCleaner[1])
            elif LineCleaner[0] == 'Train_BatchSize_From_Gui':
                if LineCleaner[1] == '-1':
                    TRAIN_BATCH_SIZE = 184
                else:
                    TRAIN_BATCH_SIZE = int(LineCleaner[1])
            elif LineCleaner[0] == 'Val_BatchSize_From_Gui':
                if LineCleaner[1] == '-1':
                    VAL_BATCH_SIZE = 46
                else:
                    VAL_BATCH_SIZE = int(LineCleaner[1])
            line = fp.readline()

    #In order to build a correct project folder hirarchy, we make sure a folder for the saved model exists, if not we make one
    try:
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, "./checkpoints")
        os.makedirs(my_file)
    except FileExistsError:
        # directory already exists
        pass

    #Creating a timestamp in order to sort the plot results
    now = datetime.now()
    TimeString = ""
    timestamp = datetime.timestamp(now)
    DateTime_object = datetime.fromtimestamp(int(timestamp))
    TimeString = DateTime_object.strftime("Date - %Y-%m-%d Time - %X") #Formatted string
    Stamp = TimeString.replace(":","_")

    HEIGHT = 300
    WIDTH = 300
    # Set the model to use the ResNet50 architecture, do not include top in order to put our own classifier.
    # Using Transfer Learning, we import the Imagenet dataset weights and we will only train the Classifier.
    base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(HEIGHT, WIDTH, 3))
    # base_model = ResNet152(weights='imagenet',include_top=False,input_shape=(HEIGHT, WIDTH, 3))

    #Directing the dataset according to the user's choice between two and three classes, scaleable to any number of classes
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    if modelType == 'Two_Classes' :
        TRAIN_DIR = os.path.join(THIS_FOLDER, "./Datasets/Two_Classes_Datasets/training")
        VAL_DIR = os.path.join(THIS_FOLDER, "./Datasets/Two_Classes_Datasets/validation")
    elif modelType == 'Three_Classes' :
        TRAIN_DIR = os.path.join(THIS_FOLDER, "./Datasets/Three_Classes_Datasets/training")
        VAL_DIR = os.path.join(THIS_FOLDER, "./Datasets/Three_Classes_Datasets/validation")


    # Image preproccessing, basic image augmentation, first we push the images throught the ImageDataGenerator,
    # then we flow in into the train and val generators, containing info needed for the model fitting.
    train_datagen = ImageDataGenerator(
        preprocessing_function=preprocess_input,
        rotation_range=90,
        horizontal_flip=True,
        vertical_flip=True,)


    val_datagen = ImageDataGenerator(
        preprocessing_function=preprocess_input,
        rotation_range=90,
        horizontal_flip=True,
        vertical_flip=True,)
    train_generator = train_datagen.flow_from_directory(VAL_DIR,
                                                        target_size=(HEIGHT, WIDTH),
                                                        batch_size=TRAIN_BATCH_SIZE,
                                                        class_mode='categorical',
                                                        shuffle=True)
    val_generator = val_datagen.flow_from_directory(TRAIN_DIR,
                                                    target_size=(HEIGHT, WIDTH),
                                                    batch_size=VAL_BATCH_SIZE,
                                                    class_mode='categorical',
                                                    shuffle=True)

    from keras.layers import Dense, Activation, Flatten, Dropout
    from keras.models import Sequential, Model
    from keras.regularizers import l1


    # Function used to build the model
    def build_finetune_model(base_model, l1_Reg, dropout, fc_layers, num_classes):
        # Set layers of our base ResNet model to not be trainable to save training time.
        for layer in base_model.layers:
            layer.trainable = False
        # Flatten the vector
        x = base_model.output
        x = Flatten()(x)
        # Add a Fully connected layer, which is trainable. added dropout, regularization and
        for fc in fc_layers:
            # New FC layer, random init
            x = Dense(fc, activation='relu', kernel_regularizer=l1(l1_Reg))(x)
            x = Dropout(dropout)(x)

        # New softmax layer
        predictions = Dense(num_classes, activation='softmax')(x)

        finetune_model = Model(inputs=base_model.input, outputs=predictions)

        return finetune_model



    FC_LAYERS = [128, 128]
    dropout = 0.5

    # Import a model if we have one saved, to continue training from the last training, else make a new one
    # C:\Users\alipkine\PycharmProjects\Test\checkpoints\Two_Classes\ResNet50_model.h5
    modelPath = "./checkpoints/" + modelType + "/" + "ResNet50_model.h5"
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, modelPath)
    if os.path.exists(my_file) and Train_new == False:
        print('Model named ' + modelType + ' Successfully loaded')
        finetune_model = tf.keras.models.load_model(my_file)
    else:
        print('Building new model')
        finetune_model = build_finetune_model(base_model,
                                              l1_Reg=l1_Reg,
                                              dropout=dropout,
                                              fc_layers=FC_LAYERS,
                                              num_classes=len(class_list))

        adam = Adam(lr=LR_Adam)
        # finetune_model.compile(adam, loss='categorical_crossentropy', metrics=['accuracy'])
        finetune_model.compile(adam, loss='categorical_crossentropy',
                               metrics=[metrics.categorical_accuracy, 'accuracy', 'acc'])

    from livelossplot import PlotLossesKeras
    # filepath="./checkpoints/" + "  ResNet152" + "_model_weights.h5"
    checkpoint = ModelCheckpoint(my_file, monitor=["acc"], verbose=1, mode='max')
    callbacks_list = [checkpoint]  # ,PlotLossesKeras()

    # Present the model's structure
    finetune_model.summary()
    # Training the model using trian and val datasets set up at the top of the file
    Start_time = time.time()
    history = finetune_model.fit_generator(train_generator, epochs=NUM_EPOCHS, workers=8,
                                           steps_per_epoch=num_train_images // TRAIN_BATCH_SIZE,
                                           validation_data=val_generator,
                                           validation_steps=num_val_images // VAL_BATCH_SIZE,
                                           shuffle=True, callbacks=callbacks_list)
    End_time = time.time()

    # list all data in history for current training, both loss and accuracy compared between the training and validation sets. also save the tables locally.
    print(history.history.keys())
    # summarize history for accuracy
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('model accuracy' + str(class_list))
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'validate'], loc='upper left')
    figAcc = plt.gcf()
    plt.show()
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, "./checkpoints/" + modelType + "/" + Stamp + "_Accuracy.jpeg")
    figAcc.savefig(my_file)

    # summarize history for loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss' + str(class_list))
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'validate'], loc='upper left')
    figLoss = plt.gcf()
    plt.show()
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, "./checkpoints/" + modelType + "/" + Stamp + "_Loss.jpeg")
    figLoss.savefig(my_file)
    #Runtime in minutes
    Run_time = (End_time - Start_time) // 60



    model_json = base_model.to_json()
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, "./model.json")
    with open(my_file, "w") as json_file:
        json_file.write(model_json)
    base_model.save_weights("./weights.h5")
    return Run_time
