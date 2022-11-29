


from PyQt5 import QtCore, QtGui, QtWidgets
from Evaluations import ml_performance
from Graph import view
from SpamDetection import Ui_Detection
from PerformanceTable import performance
class Ui_AdminHome(object):

    def classification_results(self):
        data2, accuracy_knn, accuracy_nb, accuracy_svm=ml_performance()
        list = []
        list.clear()
        list.append(float(accuracy_knn))
        list.append(float(accuracy_nb))
        list.append(float(accuracy_svm))



        view(list)

        self.Dialog = QtWidgets.QDialog()
        self.ui = performance()
        self.ui.setupUi(self.Dialog)
        self.ui.view(data2)
        self.Dialog.show()

    def spam_detection(self):

        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Detection()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()




    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(933, 666)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -50, 931, 771))
        self.label.setStyleSheet("image: url(../Detect_SpamMail/images/spam_email.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(330, 180, 351, 61))
        self.pushButton.setStyleSheet("background-color: rgb(162, 108, 81);\n"
"font: 18pt \"Franklin Gothic Heavy\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.classification_results)

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(322, 330, 361, 61))
        self.pushButton_2.setStyleSheet("background-color: rgb(162, 108, 81);\n"
"font: 18pt \"Franklin Gothic Heavy\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.spam_detection)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AdminHome"))
        self.pushButton.setText(_translate("Dialog", "Classification Results"))
        self.pushButton_2.setText(_translate("Dialog", "EMAIL SPAM DETECTION"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_AdminHome()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
