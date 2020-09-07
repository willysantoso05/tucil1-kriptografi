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
        self.cipher_text = ''
        self.plain_text = ''

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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.encryptButton = QtWidgets.QPushButton(self.groupBox)
        self.encryptButton.setObjectName("encryptButton")
        self.horizontalLayout.addWidget(self.encryptButton, 0,
                                        QtCore.Qt.AlignHCenter)
        self.decryptButton = QtWidgets.QPushButton(self.groupBox)
        self.decryptButton.setObjectName("decryptButton")
        self.horizontalLayout.addWidget(self.decryptButton, 0,
                                        QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addWidget(self.groupBox)
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
        self.horizontalLayout_4.addWidget(self.cipherGroupBox, 0,
                                          QtCore.Qt.AlignVCenter)
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
        self.space = QtWidgets.QRadioButton(self.groupBox_3)
        self.space.setChecked(True)
        self.space.setObjectName("space")
        self.verticalLayout_3.addWidget(self.space)
        self.fiveLetters = QtWidgets.QRadioButton(self.groupBox_3)
        self.fiveLetters.setObjectName("fiveLetters")
        self.verticalLayout_3.addWidget(self.fiveLetters)
        self.cipherText = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.cipherText.setObjectName("cipherText")
        self.cipherText.setReadOnly(True)
        self.verticalLayout_3.addWidget(self.cipherText)
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

        self.space.toggled.connect(self.groupInOne)
        self.fiveLetters.toggled.connect(self.groupInFive)

        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.saveFile)

        self.cipher.render(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("MainWindow", "Input Text"))
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
        self.cipherChooser.setItemText(3,
                                       _translate("MainWindow", "Hill Cipher"))
        self.cipherChooser.setItemText(
            4, _translate("MainWindow", "Enigma Cipher"))
        self.cipherChooser.setItemText(
            5, _translate("MainWindow", "Super Encrypt Cipher"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Output Text"))
        self.space.setText(_translate("MainWindow", "Without space"))
        self.fiveLetters.setText(_translate("MainWindow",
                                            "Group in 5 letters"))
        self.decryptButton.setToolTip(
            _translate("MainWindow", "Decrypt the plain text"))
        self.decryptButton.setText(_translate("MainWindow", "Decrypt"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(
            _translate("MainWindow", "Open input file as text"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(
            _translate("MainWindow", "Save output file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))

    def encrypt_clicked(self):
        input_text = self.plainText.toPlainText()
        self.cipher_text = self.cipher.encrypt(input_text)
        if (self.space.isChecked()):
            self.groupInOne()
        else:
            self.groupInFive()

    def decrypt_clicked(self):
        input_text = self.plainText.toPlainText()
        self.cipher_text = self.cipher.decrypt(input_text)
        if (self.space.isChecked()):
            self.groupInOne()
        else:
            self.groupInFive()

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
        self.cipher.render(self)

    def groupInFive(self):
        resultText = ' '.join([
            self.cipher_text[idx:idx + 5]
            for idx in range(0, len(self.cipher_text), 5)
        ])
        self.cipherText.setPlainText(resultText)

    def groupInOne(self):
        self.cipherText.setPlainText(self.cipher_text)

    def openFile(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Select Input File",
            "",
            "All Files (*)",
        )
        if fileName:
            with open(fileName, 'r') as f:
                self.plainText.setPlainText(f.read())

    def saveFile(self):
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(
            None,
            "Select File to Save Output Text",
            "",
            "All Files (*)",
        )
        if fileName:
            with open(fileName, 'w') as f:
                f.write(self.cipherText.toPlainText())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
