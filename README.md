
<p><span style="font-size: 32pt">IMAGE-Classifier </span></p>

<p>_____________________________________________________________________</p>

<p>To run this program you need: </p>
<ol>
  <li>python 2.7. </li>
  <li>liblinear.  </li>
  <li>PIL. </li>
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

<p></p>

<p>1 extracting dense SIFT features from all training images.</p>

<p>2 Saving data to file.</p>

<p>3 Feeding the Logistic regression model with data.</p>

<p>4 Saving the model.</p>

<p></p>

<p>Testing consists of:</p>

<p></p>

<p>1 Extracting dense SIFT from a test image.</p>

<p>2 testing the saved model with the test image.</p>

<p>3 Output : predicted labels.</p>

<p></p>

<p></p>
</body>
</html>
