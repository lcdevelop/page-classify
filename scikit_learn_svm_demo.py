# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import numpy as np
import urllib
from sklearn import metrics
from sklearn.svm import SVC

model = SVC()
#url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
#raw_data = urllib.urlopen(url)
#dataset = np.loadtxt(raw_data, delimiter=",")
#X = dataset[:,0:7]
#y = dataset[:,8]

x = np.ndarray((3,5))
avg=1+2+3+4+5
x[0] = np.array([1,2,3,4,5])*1.0/avg
x[1] = np.array([5,4,3,2,1])*1.0/avg
x[2] = np.array([3,3,3,3,3])*1.0/avg
y = np.array([1,2,3])
print x
print y
model.fit(x, y)
expected = y
z = np.ndarray((1, 5))
z[0] = np.array([500, 400, 300, 200, 100])*1.0/(500+400+300+200+100)
predicted = model.predict(z)
print predicted
#print(metrics.classification_report(expected, predicted))
#print(metrics.confusion_matrix(expected, predicted))
