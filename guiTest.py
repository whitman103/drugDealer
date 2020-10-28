from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from PyQt5.QtCore import Qt

class mainWindow(object):
    def setupApp(self,MainWindow):
        MainWindow.resize(400,200)
        self.mainWidget=QtWidgets.QWidget(MainWindow)

        self.pushButton=QtWidgets.QPushButton(self.mainWidget)
        self.pushButton.setGeometry(QtCore.QRect(200,100,95,30))

        self.pushButton.clicked.connect(self.changeButtonText)

        self.label=QtWidgets.QLabel(self.mainWidget)
        self.label.setGeometry(QtCore.QRect(150,60,200,10))

        self.label.setText("")

        MainWindow.setCentralWidget(self.mainWidget)
        self.retranslateUI(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def changeButtonText(self):
        self.label.setText("You did it!")

        self.pushButton.hide()

    def retranslateUI(self,MainWindow):
        Translate=QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(Translate("MainWindow","MainWindow"))
        self.pushButton.setText(Translate("MainWindow","Push Button"))

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)

    MainWindow=QtWidgets.QMainWindow()
    ui=mainWindow()
    ui.setupApp(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())