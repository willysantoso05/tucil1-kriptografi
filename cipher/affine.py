from main import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets

from .base import Base

NUMBER_OF_ALPHABET = 26

class Affine(Base):
    def __init__(self):
        super().__init__()

    def encrypt(self, plain_text: str, *args, **kwargs) -> str:
        if(self.validate(plain_text)):
            list_int_plain_text = Base.str_to_list_int(plain_text.lower(), *args, **kwargs)
            list_int_cipher_text = []

            for i in range(len(list_int_plain_text)):
                if(list_int_plain_text[i]>=0 and list_int_plain_text[i]<NUMBER_OF_ALPHABET):
                    list_int_cipher_text.append((list_int_plain_text[i] * int(self.key_m) + int(self.key_b)) % NUMBER_OF_ALPHABET)
                else:
                    list_int_cipher_text.append(list_int_plain_text[i])

            return Base.list_int_to_str(list_int_cipher_text, *args, **kwargs)

        return ''

    def decrypt(self, cipher_text: str, *args, **kwargs) -> str:
        if(self.validate(cipher_text)):
            list_int_cipher_text = Base.str_to_list_int(cipher_text.lower(), *args, **kwargs)
            list_int_plain_text = []

            m_inverse = Base.modInverse(int(self.key_m), NUMBER_OF_ALPHABET)

            for i in range(len(list_int_cipher_text)):
                if(list_int_cipher_text[i]>=0 and list_int_cipher_text[i]<NUMBER_OF_ALPHABET):
                    list_int_plain_text.append((m_inverse * (list_int_cipher_text[i] - int(self.key_b))) % NUMBER_OF_ALPHABET)
                else:
                    list_int_plain_text.append(list_int_cipher_text[i])

            return Base.list_int_to_str(list_int_plain_text, *args, **kwargs)

        return ''

    def validate(self, inputText:str) -> bool:
        #Validate :
        #1. key_m must be an integer that coprime to 26
        #2. key_b must be an integer
        #3. Input text must not be empty

        self.key_m = Base.remove_punctuation(self.key_M_Input.text(), '[^0-9]')
        self.key_b = Base.remove_punctuation(self.key_B_Input.text(), '[^0-9]')

        if(len(self.key_m)!=0 and len(self.key_b)!=0 and self.key_m!='0' and len(inputText)!=0):
            try:
                key_m = int(self.key_m)
                key_b = int(self.key_b)

                if(Base.isCoprime(key_m, NUMBER_OF_ALPHABET)):
                    return True

            except:
                print("INVALID KEY TYPE")

        return False

    def render(self, window: Ui_MainWindow):
        self.groupBox = QtWidgets.QGroupBox(window.cipherWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_KeyM = QtWidgets.QVBoxLayout()
        self.verticalLayout_KeyM.setObjectName("verticalLayout_KeyM")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout_KeyM.addWidget(self.label)
        self.key_M_Input = QtWidgets.QLineEdit(self.groupBox)
        self.key_M_Input.setObjectName("key_M_Input")
        self.verticalLayout_KeyM.addWidget(self.key_M_Input)
        self.verticalLayout.addLayout(self.verticalLayout_KeyM)
        self.verticalLayout_KeyB = QtWidgets.QVBoxLayout()
        self.verticalLayout_KeyB.setObjectName("verticalLayout_KeyB")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_KeyB.addWidget(self.label_2)
        self.key_B_Input = QtWidgets.QLineEdit(self.groupBox)
        self.key_B_Input.setObjectName("key_B_Input")
        self.verticalLayout_KeyB.addWidget(self.key_B_Input)
        self.verticalLayout.addLayout(self.verticalLayout_KeyB)
        window.verticalLayout_4.addWidget(self.groupBox)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("MainWindow", "Key"))
        self.label.setText(_translate("MainWindow", "M Coefficient (integer coprime with 26)"))
        self.label_2.setText(_translate("MainWindow", "B Coefficient (number of shifts)"))
