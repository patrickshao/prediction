"""
Huu Le

classifier.py contains methods for utilizing various
learning algorithms. Refer to each function for more
information.
"""

import numpy as np
import copy

def gaussNB():
    """
    Sample code using Gaussian Naive Bayes. This code does not
    actually apply to our problem. Use this as a reference.

    X = the initial training set; The set is a vector (list)
        of samples vectors to train the machine. This will used in fit()
    y = the label vectors; Each value corresponds to the sample vector in X.
        Therefore, the size of y MUST be the same size as the number of sample
        vectors in X.
    """

    from sklearn.naive_bayes import GaussianNB

    #Set up the list values
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    Y = np.array([1, 1, 1, 2, 2, 2])
    
    #Initialize the Naive Bayes and start training
    clf = GaussianNB()
    clf.fit(X, Y)
    GaussianNB()

    #Predict a value and print it out
    print "Training Data: ", X
    print "Labels for Training Data: ", Y
    print(clf.predict([[-0.8, -1]]))

def multNB(trainingData,trainingLabels):
    """
    Uses Multinomial Naive Bayes, which takes in 
    training data in the from of vectors, and returns a
    classifier. Note: The size of trainingLabels and 
    trainingData should bethe same size
    """

    #Check to ensure same size
    if not(len(trainingLabels) == len(trainingData)):
        print "Error: Labels and Data are of different sizes: cannot train."
        return;

    #Import from scikit and fit the data into the algorithm
    from sklearn.naive_bayes import MultinomialNB
    clf = MultinomialNB()
    clf.fit(trainingData, trainingLabels)
    MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
    return clf

def chooseClassifier(switch, trainingData,trainingLabels):
    """
    chooseClassifier() is the main method that will call different
    machine learning algorithms. The algorithm is based on what 
    'switch' value is passed in. Returns a classifier
    """
    if switch == 1:
        gaussNB()
    if switch == 2:
        return multNB(trainingData,trainingLabels)
        #We can add more if's if we want later...
    #if switch == 3:

def predict(switch, clf, newData):
    """
    Takes in a classifier and data and returns a prediction
    """
    return clf.predict(newData)


def extractFile(filename):
    """
    Takes in a filename holding the training data and
    returns a tuple of the trainingLabels and the trainingData.
    Assumes that the first value of each row is the label.
    """
    dataset = np.loadtxt(filename, delimiter=",")
    tempData = []
    tempLabels = []
    for x in range(len(dataset)):
        tempLabels.append(dataset[x][0])
        tempData.append(dataset[x][1:])
    return (np.array(tempData),np.array(tempLabels))

#Testing code 
data = np.array([])
labels = np.array([])
(data,labels) = extractFile("temp.csv")
clf = chooseClassifier(2,data,labels)
p = predict(2,clf,np.array([2,5,0,1,0,0]))
print p 