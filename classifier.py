"""
Huu Le

classifier.py contains methods for utilizing various
learning algorithms. Refer to each function for more
information.
"""

import numpy as np
import copy

def gaussNB(trainingData,trainingLabels):
    """
    Implements a Gaussian Bayes Classifier to take in
    the training data/labels and returns a classifier.
    """

    #Initialize the Naive Bayes and start training
    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    clf.fit(trainingData,trainingLabels)
    GaussianNB()

    print "Gaussian Naive Bayes Classifier has been generated with a training set size of ",len(trainingLabels) ,"."
    return clf

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
        return

    #Import from scikit and fit the data into the algorithm
    from sklearn.naive_bayes import MultinomialNB
    clf = MultinomialNB()
    clf.fit(trainingData, trainingLabels)
    MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)

    print "Multinomial Naive Bayes Classifier has been generated with a training set size of ",len(trainingLabels) ,"."
    return clf

def svmClassifier(trainingData,trainingLabels):
    """
    Uses Support Vector Machine (SVM) as the algorithm as
    the classifier. The 'kernel' param is used to determine
    which kernel function to use. We are currently using rbf, the default.
    """
    #Check to ensure same size
    if not(len(trainingLabels) == len(trainingData)):
        print "Error: Labels and Data are of different sizes: cannot train."
        return
    #Import svm from scikit and fit the data into the classifier
    from sklearn.svm import SVC
    k = 'rbf'
    clf = SVC(kernel='rbf')
    clf.fit(trainingData, trainingLabels)  

    print "Support Vector Classifier with kernel:", k," has been generated with a training set size of",len(trainingLabels)
    return clf

def perceptron(trainingData,trainingLabels):
    """
    Implements a linear perceptron model as the
    machine learning algorithm.
    """
    from sklearn.linear_model import Perceptron
    clf = Perceptron()
    clf.fit(trainingData,trainingLabels)
    
    print "Perceptron has been generated with a training set size of",len(trainingLabels)
    return clf

def sgdClassifier(trainingData,trainingLabels):
    """
    Implements Stochastic Gradient Descent as a classifier
    to use as the learning algorithm.
    """
    from sklearn.linear_model import SGDClassifier
    clf = SGDClassifier(loss="hinge", penalty="l2")
    clf.fit(trainingData, trainingLabels)
    
    print "Stochastic Gradient Descent Classifier generated with a training set size of",len(trainingLabels)
    return clf

def chooseClassifier(switch, trainingData,trainingLabels):
    """
    chooseClassifier() is the main method that will call different
    machine learning algorithms. The algorithm is based on what 
    'switch' value is passed in. Returns a classifier
    """
    if switch == 1:
        print "Switch 1: Running a Gaussian Bayes Classifier."
        return gaussNB(trainingData,trainingLabels)
    if switch == 2:
        print "Switch 2: Running a Multinomial Bayes Classifier."
        return multNB(trainingData,trainingLabels)
    if switch == 3:
        print "Switch 3: Running an SVM Classifier."
        return svmClassifier(trainingData,trainingLabels)
    if switch == 4:
        print "Switch 4: Running a Perceptron."
        return perceptron(trainingData,trainingLabels)
    if switch == 5:
        print "Switch 5: Running Stochastic Gradient Descent"
        return sgdClassifier(trainingData,trainingLabels)

def predict(clf, newData):
    """
    Takes in a classifier and data and returns a prediction
    """
    return clf.predict(newData)

#Less efficient version of testAccuracy
def testAccuracy(clf,validationData,validationLabels):
    """
    Given a declared classifier and validation data, run the
    classifier on these sample values and record the accuracy.
    Prints out the final accuracy at the end and returns it.
    """
    size = len(validationLabels)
    correct = 0.0
    for x in range(size):
        tru = validationLabels[x]
        est = clf.predict(validationData[x])
        if int(est) == int(tru):
            correct += 1
        #else:
            #print "Estimation failed: ", est, " when correct label is ", tru
            #print "Classifier's Guesses: ", clf.predict_proba(validationData[x])
    accuracy = correct/size
    print "Number correct:", correct, "out of", size,"; Accuracy:", accuracy*100, "%"
    return accuracy

def testAccuracy2(clf,validationData,validationLabels):
    """
    Given a declared classifier and validation data, run the
    classifier and print the accuracy of the classifier. Returns
    the accuracy as a decimal at the end for comparison.
    """
    accuracy = clf.score(validationData,validationLabels)
    print "Scoring classifier... Accuracy:", accuracy*100, "%"
    return accuracy

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
(data,labels) = extractFile("train.csv")
(valData,valLabels) = extractFile("validate.csv")
clf = chooseClassifier(1,data,labels)
testAccuracy(clf,valData,valLabels)
clf = chooseClassifier(2,data,labels)
testAccuracy(clf,valData,valLabels)
clf = chooseClassifier(3,data,labels)
testAccuracy(clf,valData,valLabels)
clf = chooseClassifier(4,data,labels)
testAccuracy(clf,valData,valLabels)
clf = chooseClassifier(5,data,labels)
testAccuracy(clf,valData,valLabels)