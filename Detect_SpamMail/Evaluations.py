

import sys
import pandas as pd
from sklearn import svm
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
#import metrics libraries

from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score,accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier

from sklearn.naive_bayes import MultinomialNB
import string
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def ml_performance():

    try:
        train= pd.read_csv("spam_train.csv")

        emails=train['Emails']


        tfidf = TfidfVectorizer(stop_words='english', use_idf=False, smooth_idf=False)  # TF-IDF

        X = tfidf.fit_transform(emails)  # Fit the Data

        y = train["Class"]
        #print(y)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=110)

        #Support Vector Machine
        clf_svm=svm.SVC()

        clf_svm.fit(X_train, y_train)

        predicted = clf_svm.predict(X_test)

        accuracy_svm = accuracy_score(y_test, predicted) * 100

        precision_svm = precision_score(y_test, predicted, average="macro") * 100

        recall_svm = recall_score(y_test, predicted, average="macro") * 100

        fscore_svm = f1_score(y_test, predicted, average="macro")*100

        print("SVM:")
        print("Accuracy=",accuracy_svm)
        print("Precision=",precision_svm)
        print("Recall=",recall_svm)
        print("fscore=",fscore_svm)

        # KNN
        clf_knn = KNeighborsClassifier(n_neighbors=3)

        clf_knn.fit(X_train, y_train)

        predicted = clf_knn.predict(X_test)

        accuracy_knn = accuracy_score(y_test, predicted) * 100

        precision_knn = precision_score(y_test, predicted, average="macro") * 100

        recall_knn = recall_score(y_test, predicted, average="macro") * 100

        fscore_knn = f1_score(y_test, predicted, average="macro") * 100

        print("KNN:")
        print("Accuracy=", accuracy_knn)
        print("Precision=", precision_knn)
        print("Recall=", recall_knn)
        print("fscore=", fscore_knn)

        # NB
        clf_nb = MultinomialNB(alpha=2.0)

        clf_nb.fit(X_train, y_train)

        predicted = clf_nb.predict(X_test)

        accuracy_nb = accuracy_score(y_test, predicted) * 100

        precision_nb = precision_score(y_test, predicted, average="macro") * 100

        recall_nb = recall_score(y_test, predicted, average="macro") * 100

        fscore_nb = f1_score(y_test, predicted, average="macro") * 100

        print("NB:")
        print("Accuracy=", accuracy_nb)
        print("Precision=", precision_nb)
        print("Recall=", recall_nb)
        print("fscore=", fscore_nb)

        data1 = []

        data11 = []

        data3 = []

        data2 = []

        data1.append("KNN")
        data1.append(accuracy_knn)
        data1.append(precision_knn)
        data1.append(recall_knn)
        data1.append(fscore_knn)
        data2.append(data1)

        data11.append("NB")
        data11.append(accuracy_nb)
        data11.append(precision_nb)
        data11.append(recall_nb)
        data11.append(fscore_nb)
        data2.append(data11)

        data3.append("SVM")
        data3.append(accuracy_svm)
        data3.append(precision_svm)
        data3.append(recall_svm)
        data3.append(fscore_svm)

        data2.append(data3)

        return data2, accuracy_knn, accuracy_nb, accuracy_svm

    except Exception as e:
        print("Err=" + str(e.args[0]))
        tb = sys.exc_info()[2]
        print(tb.tb_lineno)
        print(e)
#ml_performance()