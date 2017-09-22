# lego-vision
Image classification of lego parts

This project uses Keras with a TensorFlow backend to perform image classification on 678 classes of lego parts.  The script ```legos.py``` reads in the image corpus, generates additional data with `ImageDataGenerator`, constructs a convolutional neural network, and trains the model.  `setUpFolders.py' processes images in a single folder and sets up a nested folder structure for training and validation images organized by class.
