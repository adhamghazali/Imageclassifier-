from numpy import *
import numpy as np
import Image
import matplotlib as plt
import os
from liblinearutil import *
from collections import Counter
import cPickle as pickle

from dsift import dsift
from scipy.misc import imread, imresize
'''
IMAGE Classification Demo Using Logistic Regression
Adham Ghazali
'''
class trainXY:
	def __init__(self):
		self.model='cats_vs_dogs_test' 
		self.resultsdir='results'# the main directory to save the results
		
		self.current=os.getcwd()
		self.dir_path = os.path.join(self.current,self.resultsdir,self.model)
		self.testDir()
		self.Datafile=self.dir_path+'/'+'Data'
                self.Labelfile=self.dir_path+'/'+'LABELS'
		self.modelpath=self.dir_path+'/'+self.model # the model directory to save the data and results


		print 'training class initialized'
	def testDir(self):
    		
    		if not os.path.exists(self.dir_path):
			print 'making a new dir'
        		os.makedirs(self.dir_path)
	def saveData(self,Data,LABELS):
		

		np.save(self.Datafile,Data)
		

                with open(self.Labelfile, "wb") as f:
                        pickle.dump(LABELS, f)

		#with open(PIK, "rb") as f: 
			#A= pickle.load(f)


		
	def imgList(self,Directory):
		return os.listdir(Directory)

	def numClass(self,folderList):
		return len(folderList)

	def loadImage(self,source):
		return Image.open(source)
	def toGray(self, img):
		return img.convert('L')
	

	def Most_Common(self,lst,rank):
    		data = Counter(lst)
    		return data.most_common(rank)[0][0]


	def standerizeImage(self,img):

		img = array(img, 'float32')
		if img.shape[0] > 200:
        		resize_factor = 200.0 / img.shape[0]  # don't remove trailing .0 to avoid integer devision
        		img = imresize(img, resize_factor)
    		if amax(img) > 1.1:
        		img = img / 255.0
    		assert((amax(img) > 0.01) & (amax(img) <= 1))
    		assert((amin(img) >= 0.00))

    		return img


	
	def getFeatures(self,imagedata):
    		im = self.standerizeImage(imagedata)
		
    		frames, descrs = dsift(im,verbose=False,fast=True, 
				       sizes=[4, 6, 8, 10],step=2,color='rgb', 
				       floatdescriptors=False,magnif=6,
            			       windowsize=1.5,contrastthreshold=0.0)


    		return frames, descrs


	

	def getallFeatures(self,all_images,d):
		descrs=[]
	
		for i in all_images:
			source=d+'/'+i

			print 'processing ', source


            		im = self.loadImage(source)
			desc=self.getFeatures(im)[1]
            		descrs.append(desc) # we only need the discriptors
			#print 'this',descrs.shape
		descrs = hstack(descrs)

		return descrs

	def prepareData(self,Directory):
		source=self.imgList(Directory)
		nclass=self.numClass(source)
		print 'number of classes= ', nclass
		Data=[]
                LABELS=[]
		counter=0
	
		for i in source:
			
			d=Directory+'/'+i
			print d
			l=self.imgList(d)
			print l
			data=self.getallFeatures(l,d)

			labels=[counter]*len(data[0])
			print len(labels)
			LABELS.extend(labels)
			Data.append(data)
			counter=+1
		#Data=Data.tolist()
		Data= hstack(Data)
		#save the data to file
		self.saveData(Data,LABELS)
		
		return Data, LABELS
	def trainxy(self,X,Y):
		prob  = problem(Y, X)
		param = parameter('-s 7 -c 4 -B 1')
		m = train(prob, param)
		
		save_model(self.modelpath, m)
		print 'Model: ',self.modelpath,'is saved'
		return m

	def predictxy(self,x,y):
		m = load_model(self.modelpath)
		if y==None:
			y = [None] * len(x) 
		else:
			y=[y]*len(x)
		
		print '#unknown labels, put the real labels if you want to'
		p_label, p_acc, p_val = predict(y, x, m, '-b 1')


		#p_label is the predicted label
		return p_label, p_acc, p_val
	def loadData(self):
		if os.path.isfile(str(self.Datafile+'.npy'))==True:
			print "Loading data"
			Data = np.load(str(self.Datafile+'.npy'))
			
			with open(self.Labelfile, "rb") as f:
                                LABELS= pickle.load(f)
		else:
			Data, LABELS=self.prepareData('data/traintest')
		
		return Data,LABELS

 

	def main(self):
		
		Data, LABELS=self.loadData()
	        #Data, LABELS=self.prepareData('data/train')
	 	print 'processing data'
		Data=(Data.T).tolist()
		print 'training started'
		m=self.trainxy(Data,LABELS)
		print 'training is done'

	def test(self):
		d='data/test'
		source=self.imgList(d)
		#load the images inside the test directory
		for i in source:
			print i
			s=d+'/'+i
			img=self.loadImage(s)
			desc=self.getFeatures(img)[1] # only the descriptors are needed
			desc=(desc.T).tolist()
			y=0
			p_label, p_acc, p_val=self.predictxy(desc,y)
			print self.Most_Common(p_label,rank=1)# change rank to 2 to get the second most common match
	

trainer=trainXY()
trainer.test()
