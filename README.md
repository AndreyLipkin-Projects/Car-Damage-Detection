# Car-Damage-Detection
Car damage detection and classification using deep learning, implemented using libraries such as Keras and Tensorflow, with GUI and configuration files for admin.

Welcome to the source code of our final project!
In this section we will explain how to setup your environment in order to be able to run the code, since it has specific requierments - as python is an open source language and every change made by the community reflects directly on the usability of your environment.

We advice you to create a virtual environment, and make it's iteration as the interpreter of the project, in order to not mess up your current working environment's dependencies.



TIPS:

-You are requiered to download python 3.6.x version, not the latest 3.7 since some tensorflow modules still do not work in conjunction with it.
-This tutorial section will use Anaconda/Miniconda commands, since it helps you download any dependancy using wheels, making it smoother to setup rather than installing via your IDE, i.e. Pycharm.

Once you have Anaconda installed, create your virtual environment and install the dependancies using the next commands :
conda --name "Your environment name here" python=3.6

Once installed, proceed and activate it, using :

conda activate "Your environment name here"

Now let's install the project's dependancies : 

pip install --upgrade sklearn

pip install --upgrade pandas

pip install --upgrade pandas-datareader

pip install --upgrade matplotlib

pip install --upgrade pillow

pip install --upgrade requests

pip install --upgrade h5py

pip install --upgrade psutil

pip install --upgrade tensorflow==1.12.0

pip install --upgrade keras==2.2.4

We advise you use Pycharm IDE in order to view and run our source code. If you followed the instructions so far, when opening the IDE you will have an option to choose an Existing Interpreter, where you can navigate to the location of your Virtual Environment, usually at C:\Users\"Your user name"\miniconda\envs\"Your environment name"\python.exe


