#The classifer
#Read CSV files, and run the naive bayes

def classify(switch):
    if switch == 1:
        useGaussBN()
    if switch == 2:
        useMultBN()
    #if switch == 3:
          

def useGaussBN():
    import numpy as np
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    Y = np.array([1, 1, 1, 2, 2, 2])
    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    clf.fit(X, Y)
    GaussianNB()
    print "x: ", X
    print "y: ", Y
    print(clf.predict([[-0.8, -1]]))

def useMultBN():
    import numpy as np
    X = np.random.randint(2, size=(9, 10))
    y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    from sklearn.naive_bayes import MultinomialNB
    clf = MultinomialNB()
    clf.fit(X, y)
    MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
    print "x: ", X
    print "y: ", y
    print "Prediction for: ", X[8]
    print clf.predict([1,1,0,1,1,0,0,1,1,0])



classify(2)