# Load the Pima Indians diabetes dataset from CSV URL
import numpy as np
import urllib
from sklearn.naive_bayes import GaussianNB
# URL for the Pima Indians Diabetes dataset (UCI Machine Learning Repository)
gnb = GaussianNB()
url = "http://goo.gl/j0Rvxq"
# download the file
raw_data = urllib.urlopen(url)
# load the CSV file as a numpy matrix

dataset = np.loadtxt(raw_data, delimiter=",")

#print(dataset.shape)

# separate the data from the target attributes
X = dataset[:,0:7]
y = dataset[:,8]
#print (X,"lol")
y_pred = gnb.fit(X,y).predict(X)
print y_pred