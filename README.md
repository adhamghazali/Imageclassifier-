IMAGE Classifier
 =======

 Requierments:
 -----------
 
 
   * python 2,7
   * Liblinear
   * numpy
   * PIL
 
 This program trains a logistic regression image classifier.


 Simply put your data in the data/train Directory as specified and type:
 
 python training.py
 
 To test the classier. put new test images in the data/test dir and type:
 
 python classify.py.
 
 The training consists of:
  1. extracting dense SIFT features from all training images.
  2. Saving data to file.
  3. Feeding the Logistic regression model with data.
  4. Saving the model.

 Testing consists of:
  1. Extracting dense SIFT from a test image.
  2. testing the saved model with the test image.
  3. Output : predicted labels.
 

 

