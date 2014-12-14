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
    clf = SVC()
    clf.fit(trainingData, trainingLabels)  
    SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3,
    gamma=0.0, kernel=k, max_iter=-1, probability=False, random_state=None,
    shrinking=True, tol=0.001, verbose=False)

    print "Support Vector Classifier with kernel: ",k ," has been generated with a training set size of ",len(trainingLabels) ,"."
    return clf

def perceptron(trainingData,trainingLabels):
    from sklearn.linear_model import Perceptron
    clf = Perceptron()
    clf.fit(trainingData,trainingLabels)
    Perceptron(penalty=None, alpha=0.0001, fit_intercept=True, n_iter=5,
    shuffle=False, verbose=0, eta0=1.0, n_jobs=1, random_state=0,
    class_weight=None, warm_start=False)
    print "Perceptron has been generated with a training set size of ",len(trainingLabels) ,"."
    return clf

def chooseClassifier(switch, trainingData,trainingLabels):
    """
    chooseClassifier() is the main method that will call different
    machine learning algorithms. The algorithm is based on what 
    'switch' value is passed in. Returns a classifier
    """
    if switch == 1:
        print "Switch 1: Running a Sample Classifier."
        gaussNB()
    if switch == 2:
        print "Switch 2: Running a Multinomial Bayes Classifier."
        return multNB(trainingData,trainingLabels)
    if switch == 3:
        print "Switch 3: Running an SVM Classifier."
        return svmClassifier(trainingData,trainingLabels)
    if switch == 4:
        print "Switch 4: Running a Perceptron."
        return perceptron(trainingData,trainingLabels)

def predict(clf, newData):
    """
    Takes in a classifier and data and returns a prediction
    """
    return clf.predict(newData)

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
        else:
            print "Estimation failed: ", est, " when correct label is ", tru
            #print "Classifier's Guesses: ", clf.predict_proba(validationData[x])
    accuracy = correct/size
    print "Number correct: ", correct, " out of ", size, "; Accuracy: ", accuracy, "%"
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
clf = chooseClassifier(4,data,labels)
testAccuracy(clf,valData,valLabels)
