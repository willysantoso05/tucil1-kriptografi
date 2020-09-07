import numpy as np
import itertools
from .base import Base
from .vigenere import Vigenere

from PyQt5 import QtCore, QtWidgets
from main import Ui_MainWindow

DEFAULT_NUM_ALPHABET = 26

class SuperEncrypt(Vigenere):
    def __init__(self):
        super().__init__()

    def encrypt(self, plain_text: str, *args, **kwargs) -> str:
        text = Base.remove_punctuation(plain_text.lower())
        if(self.validate(text)):
            x = len(text) % int(self.k_transpose)
            if(x != 0):
                text += (int(self.k_transpose) - x) * 'z'   #add Z character

            vigenere_text = super().encrypt(text)
            return self.transpose(vigenere_text)
        return ''

    def decrypt(self, cipher_text: str, *args, **kwargs) -> str:
        text = Base.remove_punctuation(cipher_text.lower())
        if(self.validate(text)):
            transpose_text = self.transpose(text)
            plain_text = super().decrypt(transpose_text)
            return plain_text
        return ''

    def validate(self, inputText:str):
        self.key = Base.remove_punctuation(self.keyText.text())
        self.k_transpose = Base.remove_punctuation(self.K_Transpose_Input.text(), '[^0-9]')

        if(len(self.key)!=0 and len(self.k_transpose)!=0 and self.k_transpose!='0' and len(inputText)!=0):
            try:
                k_transpose = int(self.k_transpose)
                return True

            except:
                print("INVALID KEY TYPE")

        return False

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
        self.K_Transpose_Input = QtWidgets.QLineEdit(self.groupBox_5)
        self.K_Transpose_Input.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.K_Transpose_Input)
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

        self.autoKeyCheckBox.stateChanged.connect(self.auto_key_mode)
        self.fullModeCheckBox.stateChanged.connect(self.full_mode)

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

    def transpose(self, text:str):
        matrix_char = [list(text[i:i+int(self.k_transpose)]) for i in range (0, len(text), int(self.k_transpose))]
        matrix_transpose = list(itertools.zip_longest(*matrix_char))
        
        result = []
        for i in range(len(matrix_transpose)):
            for j in range (len(matrix_transpose[i])):
                if(matrix_transpose[i][j]):
                    result.append(matrix_transpose[i][j])

        return ''.join(result)