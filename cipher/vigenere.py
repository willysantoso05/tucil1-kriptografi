from itertools import cycle
from random import shuffle
from typing import List

from PyQt5 import QtCore, QtWidgets

from main import Ui_MainWindow

from .base import Base


class Vigenere(Base):
    def __init__(self):
        self.auto_key = False
        self.random = False
        self.ascii = False
        super().__init__()
        self.set_matrix()

    def encrypt(self, plain_text: str, *args, **kwargs) -> str:
        if not self.ascii:
            key_now = Base.remove_punctuation(self.keyText.text())
            plain_text = Base.remove_punctuation(plain_text.lower())
        else:
            key_now = self.keyText.text()

        list_int_plain_text = Base.str_to_list_int(plain_text, base=self.base)

        if (self.auto_key):
            key_now += plain_text

        list_int_key = Base.str_to_list_int(key_now, base=self.base)

        list_int_cipher_text = [
            self.matrix[key][num]
            for key, num in zip(cycle(list_int_key), list_int_plain_text)
        ]

        return Base.list_int_to_str(list_int_cipher_text, base=self.base)

    def decrypt(self, cipher_text: str, *args, **kwargs) -> str:
        if not self.ascii:
            key_now = Base.remove_punctuation(self.keyText.text())
            self.keyText.setText(key_now)
        else:
            key_now = self.keyText.text()

        list_int_cipher_text = Base.str_to_list_int(cipher_text,
                                                    base=self.base)

        list_int_key = Base.str_to_list_int(key_now, base=self.base)

        if self.auto_key:
            list_int_plain_text = []
            for idx, num in enumerate(list_int_cipher_text):
                key = list_int_key[idx]
                plain_int = self.matrix[key].index(num)
                list_int_plain_text.append(plain_int)
                list_int_key.append(plain_int)
        else:
            list_int_plain_text = [
                self.matrix[key].index(num)
                for key, num in zip(cycle(list_int_key), list_int_cipher_text)
            ]

        return Base.list_int_to_str(list_int_plain_text, base=self.base)

    def set_matrix(self, shift: int = 1):
        '''Generate Vigenere Matrix

        if random is True then shift will not be used
        '''
        temp_matrix = list()

        if self.ascii:
            char_count = 256
            self.base = 0
        else:
            char_count = 26
            self.base = ord('a')

        for i in range(char_count):
            temp_row = [j for j in range(i, char_count + i)]

            if self.random:
                shuffle(temp_row)

            temp_row = [j % char_count for j in temp_row]
            temp_matrix.append(temp_row)

        self.matrix = temp_matrix

    def render(self, window: Ui_MainWindow):
        self.window = window
        self.groupBox_4 = QtWidgets.QGroupBox(window.cipherWidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.keyText = QtWidgets.QLineEdit(self.groupBox_4)
        self.keyText.setObjectName("keyText")
        self.horizontalLayout_3.addWidget(self.keyText)
        window.verticalLayout_4.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(window.cipherWidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.autoKeyCheckBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.autoKeyCheckBox.setObjectName("autoKeyCheckBox")
        self.verticalLayout_2.addWidget(self.autoKeyCheckBox)
        self.fullModeCheckBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.fullModeCheckBox.setObjectName("fullModeCheckBox")
        self.verticalLayout_2.addWidget(self.fullModeCheckBox)
        self.asciiCheckBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.asciiCheckBox.setObjectName("asciiCheckBox")
        self.verticalLayout_2.addWidget(self.asciiCheckBox)
        window.verticalLayout_4.addWidget(self.groupBox_5)

        self.retranslateUi()
        self.autoKeyCheckBox.stateChanged.connect(self.auto_key_mode)
        self.fullModeCheckBox.stateChanged.connect(self.full_mode)
        self.asciiCheckBox.stateChanged.connect(self.ascii_mode)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox_4.setToolTip(
            _translate("MainWindow", "Specify Vigènere key"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Key"))
        self.groupBox_5.setToolTip(
            _translate("MainWindow", "Vigènere Cipher options"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Options"))
        self.autoKeyCheckBox.setToolTip(
            _translate("MainWindow", "Use Vigènere auto-key mode"))
        self.autoKeyCheckBox.setText(_translate("MainWindow", "Auto-key"))
        self.fullModeCheckBox.setToolTip(
            _translate("MainWindow", "Random Vigènere Table"))
        self.fullModeCheckBox.setText(_translate("MainWindow", "Full Mode"))
        self.asciiCheckBox.setToolTip(
            _translate("MainWindow", "Include all ASCII character"))
        self.asciiCheckBox.setText(_translate("MainWindow", "All ASCII"))

    def ascii_mode(self, state):
        self.ascii = bool(state)
        self.set_matrix()

        if self.ascii:
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")
            self.encryptFileButton = QtWidgets.QPushButton(
                self.window.cipherWidget)
            self.encryptFileButton.setObjectName("encryptFileButton")
            self.horizontalLayout_3.addWidget(self.encryptFileButton, 0,
                                              QtCore.Qt.AlignHCenter)
            self.decryptFileButton = QtWidgets.QPushButton(
                self.window.cipherWidget)
            self.decryptFileButton.setObjectName("decryptFileButton")
            self.horizontalLayout_3.addWidget(self.decryptFileButton, 0,
                                              QtCore.Qt.AlignHCenter)
            self.window.verticalLayout_4.addLayout(self.horizontalLayout_3)

            self.encryptFileButton.setText("Encrypt File")
            self.decryptFileButton.setText("Decrypt File")

            self.encryptFileButton.clicked.connect(self.encryptFile)
            self.decryptFileButton.clicked.connect(self.decryptFile)
        else:
            self.window.clean(self.horizontalLayout_3)

    def full_mode(self, state):
        self.random = bool(state)
        self.set_matrix()

    def auto_key_mode(self, state):
        self.auto_key = bool(state)

    def encryptFile(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Select Input File",
            "",
            "All Files (*)",
        )
        print(fileName)
        # if fileName:
        #     with open(fileName, 'r') as f:
        #         self.plainText.setPlainText(f.read())

    def decryptFile(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Select Input File",
            "",
            "All Files (*)",
        )
        print(fileName)
        # if fileName:
        #     with open(fileName, 'r') as f:
        #         self.plainText.setPlainText(f.read())