<?xml version="1.0" encoding="iso-8859-1"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
      "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="content-type" content="text/html; charset=iso-8859-1" />
  <title>New</title>
  <meta name="generator" content="Amaya, see http://www.w3.org/Amaya/" />
</head>

<body>
<p>To run this program you need:</p>

<p></p>

<p>1-python 2.7. 2-liblinear. </p>

<p>3-PIL.</p>

<p>This program trains a logistic regression classifier to differentiate
between images. Simply put your data in the data/train Directory as specified
and type:</p>

<p>python training.py.</p>

<p>To test the classier. put new images in the data/test dir and type:</p>

<p>python classify.py.</p>

<p>The training consists of:</p>

<p>1 extracting dense SIFT features from all training images.</p>

<p>2 Saving data to file.</p>

<p>3 Feeding the Logistic regression model with data.</p>

<p>4 Saving the model.</p>

<p>Testing consists of:</p>

<p>1 Extracting dense SIFT from a test image.</p>

<p>2 testing the saved model with the test image.</p>

<p>3 Output : predicted labels.</p>
</body>
</html>

1	Extracting dense SIFT from a test image.

2	testing the saved model with the test image.

3	Output : predicted labels.

