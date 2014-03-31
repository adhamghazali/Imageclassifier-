<html>
<head>
  <meta http-equiv="content-type" content="text/html; charset=iso-8859-1">
  <title>New</title>
  <meta name="generator" content="Amaya, see http://www.w3.org/Amaya/">
</head>

<body>
<h4><span style="font-size: 32pt">IMAGE-Classifier</span></h4>

<h1><span style="font-size: 16pt">To run this program you need:</span></h1>
<ol>
  <li>python 2.7.</li>
  <li>liblinear. </li>
  <li>PIL.</li>
</ol>

<p>This program trains a logistic regression classifier to differentiate
between images. Simply put your data in the data/train Directory as specified
and type:</p>

<p id="python">python training.py</p>

<p></p>

<p>To test the classier. put new test images in the data/test dir and type:</p>

<p></p>

<p>python classify.py.</p>

<p></p>

<p>The training consists of:</p>

<h1></h1>
<ol>
  <li>extracting dense SIFT features from all training images.</li>
  <li>Saving data to file.</li>
  <li>Feeding the Logistic regression model with data.</li>
  <li>Saving the model.</li>
</ol>

<p></p>

<h1>Testing consists of:</h1>
<ol>
  <li>Extracting dense SIFT from a test image.</li>
  <li>testing the saved model with the test image.</li>
  <li>Output : predicted labels.</li>
</ol>

<p></p>

<p></p>
</body>
</html>
