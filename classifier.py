"""
Huu Le

classifier.py contains methods for utilizing various
learning algorithms. Refer to each function for more
information.
"""

import numpy as np
global clf

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

def multNB():
    """
    Uses Multinomial Naive Bayes, which takes in training data i nthe from
    of vectors.

    ---Note--- At the moment, it is only using dummy variables. Need to
    take in vector parameters instead!
    """
    X = np.array([[1,0],[0,0],[1,1],[0,1]])
    y = np.array([2,1,1,0])
    from sklearn.naive_bayes import MultinomialNB
    clf = MultinomialNB()
    clf.fit(X, y)
    MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
    print "Training Data: ", X
    print "Training Labels: ", y
    for x in range(10):
        a = np.random.randint(2)
        b = np.random.randint(2)
        z = np.array([a,b])
        print "Given score: ", z, "Best prediction: ",  clf.predict(z), "Probabilities: ", clf.predict_proba(z)

def chooseClassifier(switch):
    """
    chooseClassifier() is the main method that will call different
    machine learning algorithms. The algorithm is based on what 
    'switch' value is passed in.
    """
    if switch == 1:
        gaussNB()
    if switch == 2:
        multNB()
        #We can add more if's if we want later...
    #if switch == 3:

def classify(filename,switch):
    dataset = np.loadtxt(filename, delimiter=",")
    trainingData = []
    trainingLabels = []
    for x in range(len(dataset)):
        trainingLabels.append(dataset[x][0])
        trainingData.append(dataset[x][1:])
        print trainingData, trainingLabels

classify("temp.csv",2)
chooseClassifier(2)