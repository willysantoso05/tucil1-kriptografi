from PyQt5 import QtCore, QtGui, QtWidgets
from cipher import *


class Ui_MainWindow(object):
    def __init__(self):
        self.cipher = Vigenere()
        self.cipher_list = [
            Vigenere(),
            Playfair(),
            Affine(),
            Hill(), 
            Enigma(),
            SuperEncrypt()
        ]

    def setupUi(self, MainWindow: QtWidgets.QMainWindow):

        screen: QtGui.QScreen = MainWindow.screen()
        width = int(screen.size().width() / 2)
        height = int(screen.size().height() / 2.7)

        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Cipher Simulator")

        MainWindow.resize(width, height)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(width, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        # self.horizontalLayout = QtWidgets.QHBoxLayout()
        # self.horizontalLayout.setSizeConstraint(
        #     QtWidgets.QLayout.SetMinAndMaxSize)
        # self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        # self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(500, 500))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainText = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainText.setObjectName("plainText")
        self.verticalLayout.addWidget(self.plainText)
        self.encryptButton = QtWidgets.QPushButton(self.groupBox)
        self.encryptButton.setObjectName("encryptButton")
        self.verticalLayout.addWidget(self.encryptButton, 0,
                                      QtCore.Qt.AlignHCenter)
        # self.horizontalLayout.addWidget(self.groupBox)
        self.horizontalLayout_4.addWidget(self.groupBox)
        # self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.cipherGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cipherGroupBox.sizePolicy().hasHeightForWidth())   
        self.cipherGroupBox.setSizePolicy(sizePolicy)
        self.cipherGroupBox.setMinimumSize(QtCore.QSize(300, 0))
        self.cipherGroupBox.setMaximumSize(QtCore.QSize(300, 400))
        self.cipherGroupBox.setBaseSize(QtCore.QSize(0, 0))
        self.cipherGroupBox.setAlignment(QtCore.Qt.AlignLeading
                                         | QtCore.Qt.AlignLeft
                                         | QtCore.Qt.AlignVCenter)
        self.cipherGroupBox.setObjectName("cipherGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.cipherGroupBox)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.cipherWidget = QtWidgets.QWidget(self.cipherGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cipherWidget.sizePolicy().hasHeightForWidth())
        self.cipherWidget.setSizePolicy(sizePolicy)
        self.cipherWidget.setObjectName("cipherWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.cipherWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.gridLayout.addWidget(self.cipherWidget, 2, 2, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.cipherGroupBox)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cipherChooser = QtWidgets.QComboBox(self.groupBox_6)
        self.cipherChooser.setObjectName("cipherChooser")
        self.cipherChooser.addItem("")
        self.cipherChooser.addItem("")
        self.cipherChooser.addItem("")
        self.cipherChooser.addItem("")
        self.cipherChooser.addItem("")
        self.cipherChooser.addItem("")
        self.horizontalLayout_2.addWidget(self.cipherChooser)
        self.gridLayout.addWidget(self.groupBox_6, 1, 2, 1, 1)
        self.horizontalLayout_4.addWidget(self.cipherGroupBox,  0, QtCore.Qt.AlignVCenter)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(500, 500))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cipherText = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.cipherText.setObjectName("cipherText")
        self.verticalLayout_3.addWidget(self.cipherText)
        self.decryptButton = QtWidgets.QPushButton(self.groupBox_3)
        self.decryptButton.setObjectName("decryptButton")
        self.verticalLayout_3.addWidget(self.decryptButton, 0,
                                        QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4.addWidget(self.groupBox_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.encryptButton.clicked.connect(self.encrypt_clicked)
        self.decryptButton.clicked.connect(self.decrypt_clicked)
        self.cipherChooser.currentIndexChanged.connect(self.change_cipher)

        self.cipher.render(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("MainWindow", "Plain Text"))
        self.encryptButton.setToolTip(
            _translate("MainWindow", "Encrypt the plain text"))
        self.encryptButton.setText(_translate("MainWindow", "Encrypt"))
        self.cipherGroupBox.setTitle(_translate("MainWindow", "Cipher"))     
        
        self.groupBox_6.setTitle(_translate("MainWindow", "GroupBox"))
        self.cipherChooser.setItemText(
            0, _translate("MainWindow", "Vigènere Cipher"))
        self.cipherChooser.setItemText(
            1, _translate("MainWindow", "Playfair Cipher"))
        self.cipherChooser.setItemText(
            2, _translate("MainWindow", "Affine Cipher"))
        self.cipherChooser.setItemText(
            3, _translate("MainWindow", "Hill Cipher"))
        self.cipherChooser.setItemText(
            4, _translate("MainWindow", "Enigma Cipher"))
        self.cipherChooser.setItemText(
            5, _translate("MainWindow", "Super Encrypt Cipher"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Cipher Text"))
        self.decryptButton.setToolTip(
            _translate("MainWindow", "Decrypt the plain text"))
        self.decryptButton.setText(_translate("MainWindow", "Decrypt"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(
            _translate("MainWindow", "Open file to encrypt"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(
            _translate("MainWindow", "Save ciphertext"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))

    def encrypt_clicked(self):
        plain_text = self.plainText.toPlainText()
        cipher_text = self.cipher.encrypt(plain_text)
        self.cipherText.setPlainText(cipher_text)

    def decrypt_clicked(self):
        cipher_text = self.cipherText.toPlainText()
        plain_text = self.cipher.decrypt(cipher_text)
        self.plainText.setPlainText(plain_text)

    def clean(self, layout):
        for i in reversed(range(layout.count())):
            item = layout.takeAt(i)
            widget = item.widget()
            if widget is not None:
                widget.close()
            else:
                self.clean(item.layout())

    def change_cipher(self, idx: int):
        self.clean(self.verticalLayout_4)
        self.cipher = self.cipher_list[idx]
        print(self.cipher)
        self.cipher.render(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
