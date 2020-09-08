import re
from collections import OrderedDict
from math import sqrt

from PyQt5 import QtCore, QtWidgets

from main import Ui_MainWindow

from .base import Base

DEFAULT_KEY = 'abcdefghiklmnopqrstuvwxyz'
DEFAULT_WIDTH = 5


class Playfair(Base):
    def set_key(self, key):
        key = Base.remove_punctuation(key)
        key = re.sub('j', '', key)
        key += DEFAULT_KEY
        key = ''.join(OrderedDict.fromkeys(key).keys())
        self.key = key
        return (len(key) == 25)

    def _encrypt_pair_(self, a: str, b: str) -> str:
        row_a, col_a = divmod(self.key.index(a), DEFAULT_WIDTH)
        row_b, col_b = divmod(self.key.index(b), DEFAULT_WIDTH)

        cipher_a, cipher_b = '', ''
        if row_a == row_b:
            # same row
            cipher_a = self.key[row_a * DEFAULT_WIDTH +
                                (col_a + 1) % DEFAULT_WIDTH]
            cipher_b = self.key[row_b * DEFAULT_WIDTH +
                                (col_b + 1) % DEFAULT_WIDTH]
        elif col_a == col_b:
            # same col
            cipher_a = self.key[((row_a + 1) % DEFAULT_WIDTH) * DEFAULT_WIDTH +
                                col_a]
            cipher_b = self.key[((row_b + 1) % DEFAULT_WIDTH) * DEFAULT_WIDTH +
                                col_b]
        else:
            # corner
            cipher_a = self.key[row_a * DEFAULT_WIDTH + col_b]
            cipher_b = self.key[row_b * DEFAULT_WIDTH + col_a]
        return cipher_a + cipher_b

    def encrypt(self, plain_text: str, *args, **kwargs) -> str:
        if not self.set_key(self.keyText.text()):
            return ''

        plain_text = re.sub('j', 'i', plain_text)
        plain_text = Base.remove_punctuation(plain_text.lower())

        temp_char = ''

        cipher_text = []
        for idx, char in enumerate(plain_text):
            if temp_char:
                if temp_char == char:
                    cipher = self._encrypt_pair_(temp_char, 'x')
                    temp_char = char
                else:
                    cipher = self._encrypt_pair_(temp_char, char)
                    temp_char = ''
                cipher_text.append(cipher)
            else:
                if idx == len(plain_text) - 1:
                    # last but not pair
                    cipher_text.append(self._encrypt_pair_(char, 'x'))
                else:
                    temp_char = char

        return ''.join(cipher_text)

    def _decrypt_pair_(self, a: str, b: str) -> str:
        row_a, col_a = divmod(self.key.index(a), DEFAULT_WIDTH)
        row_b, col_b = divmod(self.key.index(b), DEFAULT_WIDTH)

        cipher_a, cipher_b = '', ''
        if row_a == row_b:
            # same row
            cipher_a = self.key[row_a * DEFAULT_WIDTH +
                                (col_a - 1) % DEFAULT_WIDTH]
            cipher_b = self.key[row_b * DEFAULT_WIDTH +
                                (col_b - 1) % DEFAULT_WIDTH]
        elif col_a == col_b:
            # same col
            cipher_a = self.key[((row_a - 1) % DEFAULT_WIDTH) * DEFAULT_WIDTH +
                                col_a]
            cipher_b = self.key[((row_b - 1) % DEFAULT_WIDTH) * DEFAULT_WIDTH +
                                col_b]
        else:
            # corner
            cipher_a = self.key[row_a * DEFAULT_WIDTH + col_b]
            cipher_b = self.key[row_b * DEFAULT_WIDTH + col_a]
        return cipher_a + cipher_b

    def decrypt(self, cipher_text: str, *args, **kwargs) -> str:
        if not self.set_key(self.keyText.text()):
            return ''
        cipher_text = re.sub('j', 'i', cipher_text)
        cipher_text = Base.remove_punctuation(cipher_text.lower())

        if len(cipher_text) % 2 == 1:
            # text length in odd
            cipher_text += 'x'

        return ''.join([
            self._decrypt_pair_(cipher_text[idx], cipher_text[idx + 1])
            for idx in range(0, len(cipher_text), 2)
        ])

    def render(self, window: Ui_MainWindow):
        self.groupBox_4 = QtWidgets.QGroupBox(window.cipherWidget)
        self.groupBox_4.setGeometry(QtCore.QRect(9, 9, 441, 111))
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.keyText = QtWidgets.QLineEdit(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.keyText.sizePolicy().hasHeightForWidth())
        self.keyText.setSizePolicy(sizePolicy)
        self.keyText.setObjectName("keyText")
        self.horizontalLayout_3.addWidget(self.keyText)
        window.verticalLayout_4.addWidget(self.groupBox_4)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox_4.setToolTip(
            _translate("MainWindow", "Specify Playfair key"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Key"))
