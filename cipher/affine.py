from main import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets

from .base import Base

NUMBER_OF_ALPHABET = 26

class Affine(Base):
    def __init__(self):
        super().__init__()

    def encrypt(self, plain_text: str, *args, **kwargs) -> str:
        if(self.validate()):
            if(len(Base.remove_punctuation(plain_text))!=0):
                list_int_plain_text = Base.str_to_list_int(plain_text, *args, **kwargs)
                list_int_cipher_text = []
    
                for i in range(len(list_int_plain_text)):
                    list_int_cipher_text.append((list_int_plain_text[i] * int(self.key_m) + int(self.key_b)) % NUMBER_OF_ALPHABET)
    
                return Base.list_int_to_str(list_int_cipher_text, *args, **kwargs)

        return ''

    def decrypt(self, cipher_text: str, *args, **kwargs) -> str:
        if(self.validate()):
            if(len(Base.remove_punctuation(cipher_text))!=0):
                list_int_cipher_text = Base.str_to_list_int(cipher_text, *args, **kwargs)
                list_int_plain_text = []

                m_inverse = Base.modInverse(int(self.key_m), NUMBER_OF_ALPHABET)

                for i in range(len(list_int_cipher_text)):
                    list_int_plain_text.append((m_inverse * (list_int_cipher_text[i] - int(self.key_b))) % NUMBER_OF_ALPHABET)

                return Base.list_int_to_str(list_int_plain_text, *args, **kwargs)

        return ''

    def validate(self) -> bool:
        self.key_m = Base.remove_punctuation(self.key_M_Input.text(), '[^0-9]')
        self.key_b = Base.remove_punctuation(self.key_B_Input.text(), '[^0-9]')

        if(len(self.key_m)!=0 and len(self.key_b)!=0 and self.key_m!='0'):
            try:
                key_m = int(self.key_m)
                key_b = int(self.key_b)

                if(Base.isCoprime(key_m, 26)):
                    return True

            except:
                print("INVALID KEY TYPE")

        return False

    def render(self, window: Ui_MainWindow):
        self.groupBox = QtWidgets.QGroupBox(window.cipherWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.key_M_Input = QtWidgets.QLineEdit(self.groupBox)
        self.key_M_Input.setObjectName("key_M_Input")
        self.horizontalLayout.addWidget(self.key_M_Input)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.key_B_Input = QtWidgets.QLineEdit(self.groupBox)
        self.key_B_Input.setObjectName("key_B_Input")
        self.horizontalLayout_2.addWidget(self.key_B_Input)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        window.verticalLayout_4.addWidget(self.groupBox)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("MainWindow", "Key"))
        self.label.setText(_translate("MainWindow", "M"))
        self.label_2.setText(_translate("MainWindow", "B"))
