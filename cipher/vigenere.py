from itertools import cycle
from random import shuffle
from typing import List
from main import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets


from .base import Base


class Vigenere(Base):

    def __init__(self):
        self.auto_key = False
        self.random = False
        self.ascii = False
        super().__init__()
        self.set_matrix()


    def encrypt(self, plain_text: str, *args, **kwargs) -> str:
        list_int_plain_text = Base.str_to_list_int(plain_text, *args, **kwargs)

        if(self.auto_key):
            self.key += plain_text

        list_int_key = Base.str_to_list_int(self.key, *args, **kwargs)

        list_int_cipher_text = [
            self.matrix[key][num]
            for key, num in zip(cycle(list_int_key), list_int_plain_text)
        ]

        return Base.list_int_to_str(list_int_cipher_text, *args, **kwargs)

    def decrypt(self, cipher_text: str, *args, **kwargs) -> str:

        list_int_cipher_text = Base.str_to_list_int(cipher_text, *args,
                                                    **kwargs)

        list_int_key = Base.str_to_list_int(self.key, *args, **kwargs)

        list_int_plain_text = [
            self.matrix[key].index(num)
            for key, num in zip(cycle(list_int_key), list_int_cipher_text)
        ]

        return Base.list_int_to_str(list_int_plain_text, *args, **kwargs)

    def set_matrix(self, shift: int = 1):
        '''Generate Vigenere Matrix

        if random is True then shift will not be used
        '''
        temp_matrix = list()

        if self.ascii:
            char_count = 256
        else:
            char_count = 26

        for i in range(char_count):
            temp_row = [j for j in range(i, char_count + i)]
            if self.random:
                shuffle(temp_row)
            else:
                temp_row = [j % char_count for j in temp_row]
            temp_matrix.append(temp_row)

        self.matrix = temp_matrix

    def render(self, window: Ui_MainWindow):
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
        self.autoKeyCheckBox.stateChanged.connect(lambda state: setattr(self,'auto_key', bool(state)))
        self.fullModeCheckBox.stateChanged.connect(lambda state: setattr(self,'random', bool(state)))
        self.asciiCheckBox.stateChanged.connect(lambda state: setattr(self,'ascii', bool(state)))
        self.keyText.textChanged.connect(lambda text: setattr(self,'key',text))

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