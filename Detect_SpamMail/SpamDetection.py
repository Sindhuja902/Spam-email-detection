
from PyQt5 import QtCore, QtGui, QtWidgets
from sklearn import svm
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
class Ui_Detection(object):


    def detection_spam(self):

        try:
            subject = self.plainTextEdit.toPlainText()

            train = pd.read_csv("spam_train.csv")

            emails = train['Emails']

            tfidf = TfidfVectorizer(stop_words='english', use_idf=False, smooth_idf=False)  # TF-IDF

            X_train = tfidf.fit_transform(emails)  # Fit the Data

            y_train = train["Class"]

            X_test = tfidf.transform([subject])

            clf_svm = svm.SVC()

            clf_svm.fit(X_train, y_train)

            predicted = clf_svm.predict(X_test)

            print(predicted)

            if predicted[0]=='spam':
                self.label_4.setStyleSheet("font: 75 20pt \"Times New Roman\";\n"
                                        
                                          "color: rgb(170, 0, 0);")
                self.label_4.setText("SPAM")

            else:
                self.label_4.setStyleSheet("font: 75 20pt \"Times New Roman\";\n"
                                         
                                           "color: rgb(0, 0, 0);")
                self.label_4.setText("HAM")






        except Exception as e:
            print("Err=" + str(e.args[0]))
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)





    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1027, 648)
        Dialog.setStyleSheet("background-color: rgb(188, 94, 141);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 10, 461, 521))
        self.label.setStyleSheet("image: url(../Detect_SpamMail/images/spamfilter.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(490, 150, 481, 191))
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Verdana\";")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(640, 360, 181, 51))
        self.pushButton.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(63, 126, 189);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.detection_spam)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(490, 98, 201, 51))
        self.label_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(470, 490, 101, 51))
        self.label_3.setStyleSheet("font: 75 16pt \"Verdana\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(630, 491, 101, 51))
        self.label_4.setStyleSheet("font: 75 16pt \"Verdana\";")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Email Spam Detection"))
        self.pushButton.setText(_translate("Dialog", "Detection"))
        self.label_2.setText(_translate("Dialog", "Enter Email Subject:"))
        self.label_3.setText(_translate("Dialog", "Result :"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Detection()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
