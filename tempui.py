from cipher import *

import sys
from PyQt5 import QtWidgets
from PyQt5 import uic

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("PyQT App")
        uic.loadUi('UI/mainwindow.ui', self)

        self.encryptButton = self.findChild(QtWidgets.QPushButton, 'EncryptButton')
        self.encryptButton.clicked.connect(self.encryptButtonClicked)
        self.decryptButton = self.findChild(QtWidgets.QPushButton, 'DecryptButton')
        self.decryptButton.clicked.connect(self.decryptButtonClicked)

        self.inputPlainText = self.findChild(QtWidgets.QTextEdit, 'InputPlainText')
        self.inputCipherText = self.findChild(QtWidgets.QTextEdit, 'InputCipherText')

        #Khusus Affine
        self.inputKeyM = self.findChild(QtWidgets.QLineEdit, 'InputKeyM')
        self.inputKeyB = self.findChild(QtWidgets.QLineEdit, 'InputKeyB')

    def encryptButtonClicked(self):
        plainText = Base.remove_punctuation(self.inputPlainText.toPlainText())
        key_m = Base.remove_punctuation(self.inputKeyM.text(), '[^0-9]')
        key_b = Base.remove_punctuation(self.inputKeyB.text(), '[^0-9]')
    
        if(len(plainText)!=0 and len(key_m)!=0 and len(key_b)!=0):
            try:
                key_m = int(key_m)
                key_b = int(key_b)

            except:
                raise Exception("INVALID KEY")

            if(Base.isCoprime(key_m, 26)):
                cipher = Affine(key_m, key_b)
                self.inputCipherText.setText(cipher.encrypt(plainText))
            else:
                print("KEY_M must be coprime to 26 !")

    def decryptButtonClicked(self):
        cipherText = Base.remove_punctuation(self.inputCipherText.toPlainText())
        key_m = Base.remove_punctuation(self.inputKeyM.text(), '[^0-9]')
        key_b = Base.remove_punctuation(self.inputKeyB.text(), '[^0-9]')

        if(len(cipherText)!=0 and len(key_m)!=0 and len(key_b)!=0):
            try:
                key_m = int(key_m)
                key_b = int(key_b)
            except:
                raise Exception("INVALID KEY")

            if(Base.isCoprime(key_m, 26)):
                cipher = Affine(key_m, key_b)
                self.inputPlainText.setText(cipher.decrypt(cipherText))
            else:
                print("KEY_M must be coprime to 26 !")

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    window()

