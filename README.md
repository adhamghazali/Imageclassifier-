IMAGE-Classifier
================


To run this program you need:
python 2.7.
liblinear. 
PIL.
This program trains a logistic regression classifier to differentiate between images. Simply put your data in the data/train Directory as specified and type:
python training.py
To test the classier. put new test images in the data/test dir and type:
python classify.py.
The training consists of:
extracting dense SIFT features from all training images.
Saving data to file.
Feeding the Logistic regression model with data.
Saving the model.
Testing consists of:
Extracting dense SIFT from a test image.
testing the saved model with the test image.
Output : predicted labels.
