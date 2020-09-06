import numpy as np
import itertools
from .base import Base
from .vigenere import Vigenere

from PyQt5 import QtCore, QtWidgets
from main import Ui_MainWindow

DEFAULT_NUM_ALPHABET = 26

class SuperEncrypt(Vigenere):
    # def __init__(self, key: str):
    #     super().__init__(key)
    #     super().set_matrix(DEFAULT_NUM_ALPHABET)

    def encrypt(self, plain_text: str, *args, **kwargs) -> str:
        x = len(plain_text) % self.k_transpose
        if(x != 0):
            plain_text += (self.k_transpose - x) * 'z'   #add Z character
        
        vigenere_text = super().encrypt(plain_text)
        return SuperEncrypt.transpose(vigenere_text, self.k_transpose)


    def decrypt(self, cipher_text: str, *args, **kwargs) -> str:
        transpose_text = SuperEncrypt.transpose(cipher_text, self.k_transpose)
        cipher_text = super().decrypt(transpose_text)
        return cipher_text

    def render(self, window: Ui_MainWindow):
        self.groupBox_5 = QtWidgets.QGroupBox(window.cipherWidget)
        self.groupBox_5.setGeometry(QtCore.QRect(9, 153, 267, 129))
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.autoKeyCheckBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.autoKeyCheckBox.setObjectName("autoKeyCheckBox")
        self.verticalLayout_2.addWidget(self.autoKeyCheckBox)
        self.fullModeCheckBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.fullModeCheckBox.setObjectName("fullModeCheckBox")
        self.verticalLayout_2.addWidget(self.fullModeCheckBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.groupBox_4 = QtWidgets.QGroupBox(window.cipherWidget)
        self.groupBox_4.setGeometry(QtCore.QRect(9, 9, 166, 69))
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.keyText = QtWidgets.QLineEdit(self.groupBox_4)
        self.keyText.setObjectName("keyText")
        self.horizontalLayout_3.addWidget(self.keyText)
        window.verticalLayout_4.addWidget(self.groupBox_4)
        window.verticalLayout_4.addWidget(self.groupBox_5)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox_4.setToolTip(_translate("MainWindow", "Specify Vigènere key"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Key"))
        self.groupBox_5.setToolTip(_translate("MainWindow", "Vigènere Cipher options"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Options"))
        self.autoKeyCheckBox.setToolTip(_translate("MainWindow", "Use Vigènere auto-key mode"))
        self.autoKeyCheckBox.setText(_translate("MainWindow", "Auto-key"))
        self.fullModeCheckBox.setToolTip(_translate("MainWindow", "Random Vigènere Table"))
        self.fullModeCheckBox.setText(_translate("MainWindow", "Full Mode"))
        self.label.setText(_translate("MainWindow", "K (Transpose)"))


    @staticmethod
    def transpose(text, k_transpose: int):
        matrix_char = [list(text[i:i+k_transpose]) for i in range (0, len(text), k_transpose)]
        matrix_transpose = list(itertools.zip_longest(*matrix_char))
        
        result = []
        for i in range(len(matrix_transpose)):
            for j in range (len(matrix_transpose[i])):
                if(matrix_transpose[i][j]):
                    result.append(matrix_transpose[i][j])

        return ''.join(result)