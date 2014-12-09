import numpy as np
import urllib
import csv

#fname2="E0.csv"
#r=open(fname2)


url = "E0.csv"

raw_data = urllib.urlopen(url)
#raw_data = r
dataset = np.loadcsv(raw_data, delimiter=",")

print(dataset.shape)

X= dataset[:,0:7]
Y= dataset[:8]