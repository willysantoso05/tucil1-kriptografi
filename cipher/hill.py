import numpy as np
import re
import random
import string

from PyQt5 import QtCore, QtWidgets
from main import Ui_MainWindow
from .base import Base

NUMBER_OF_ALPHABET = 26

class Hill(Base):
    def __init__(self):
        super().__init__()

    def encrypt(self, plain_text: str, *args, **kwargs) -> str:
        if(self.validate()):
            self.processingKey()
        list_int_plain_text = Base.str_to_list_int(plain_text, *args, **kwargs)
        list_int_key = Base.str_to_list_int(self.key, *args, **kwargs)

        #Convert into matrix
        matrix_int_plain_text = [list_int_plain_text[i:i+self.m_linear] for i in range (0, len(list_int_plain_text), self.m_linear)]
        while(len(matrix_int_plain_text[-1])!=self.m_linear):
            matrix_int_plain_text[-1].append(25)    #add Z character if text mod m != 0
        matrix_key = np.array([list_int_key[i:i+self.m_linear] for i in range (0, len(list_int_key), self.m_linear)])

        list_int_cipher_text = []

        for item in matrix_int_plain_text:
            multiplication_result = np.dot(matrix_key, item)
            for number in multiplication_result:
                list_int_cipher_text.append(number % NUMBER_OF_ALPHABET)
        
        return Base.list_int_to_str(list_int_cipher_text, *args, **kwargs)

    def decrypt(self, cipher_text: str, *args, **kwargs) -> str:
        list_int_cipher_text = Base.str_to_list_int(cipher_text, *args, **kwargs)
        list_int_key = Base.str_to_list_int(self.key, *args, **kwargs)

        #Convert into matrix
        matrix_int_cipher_text = [list_int_cipher_text[i:i+self.m_linear] for i in range (0, len(list_int_cipher_text), self.m_linear)]
        while(len(matrix_int_cipher_text[-1])!=self.m_linear):
            matrix_int_cipher_text[-1].append(25)    #add Z character if text mod m != 0
        matrix_key = np.array([list_int_key[i:i+self.m_linear] for i in range (0, len(list_int_key), self.m_linear)])

        determinant = int(np.linalg.det(matrix_key))
        if(determinant == 0 or not Base.isCoprime(abs(determinant), NUMBER_OF_ALPHABET)):
            raise Exception("TEXT CAN NOT BE DECRYPTED, TRY ANOTHER KEY")
        
        inverse_matrix_key =  (np.round_((np.linalg.inv(matrix_key) *determinant) * Base.modInverse(determinant, NUMBER_OF_ALPHABET))).astype(int) % NUMBER_OF_ALPHABET

        list_int_plain_text = []

        for item in matrix_int_cipher_text:
            multiplication_result = np.dot(inverse_matrix_key, item)
            for number in multiplication_result:
                list_int_plain_text.append(number % NUMBER_OF_ALPHABET)
        
        return Base.list_int_to_str(list_int_plain_text, *args, **kwargs)

    def validate(self) -> bool:
        # self.m_linear = Base.remove_punctuation(self.m_linear, '[^0-9]')
    
        # if(len(self.m_linear)!=0 self.m_linear!='0'):
        #     try:
        #         m_linear = int(self.m_linear)
        #         return True

        #     except:
        #         print("INVALID KEY TYPE")

        # print("INVALID KEY")
        return False

    def processingKey(self):
        if(len(self.key) > self.m_linear * self.m_linear):
            self.key = self.key[0:self.m_linear * self.m_linear]
        elif(len(self.key) < self.m_linear * self.m_linear):
            self.key += str(''.join(random.choices(string.ascii_uppercase, k=self.m_linear * self.m_linear-len(self.key)))) 

    def render(self, window: Ui_MainWindow):
        self.verticalLayoutWidget = QtWidgets.QWidget(window.cipherWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 321, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.keyInput = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.keyInput.setObjectName("keyInput")
        self.horizontalLayout_2.addWidget(self.keyInput)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.key_M_Input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.key_M_Input.setObjectName("key_M_Input")
        self.horizontalLayout.addWidget(self.key_M_Input)
        self.verticalLayout.addLayout(self.horizontalLayout)
        window.verticalLayout_4.addWidget(self.verticalLayoutWidget)

        self.retranslateUi()
        self.keyInput.textChanged.connect(lambda text: setattr(self,'key', Base.remove_punctuation(text)))
        self.key_M_Input.textChanged.connect(lambda text: setattr(self,'m_linear', Base.remove_punctuation(text, '[^0-9]')))

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("MainWindow", "Key"))
        self.label.setText(_translate("MainWindow", "M (Linear)"))