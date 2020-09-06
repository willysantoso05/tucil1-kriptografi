from main import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets
from typing import List

from .base import Base


class Enigma(Base):
    '''Enigma M3 cipher without ring position and plug board.
    
    :param rotors: The rotors and their order. There are 8 rotors. e.g. [3,2,1]. 
    :param position: Rotor's start positions, consists of 3 alphabet e.g. ['C','Y','P']
    :param reflector: The reflector in use, B' or 'C'
    '''
    def __init__(self,
                 rotors: List[int] = [1, 2, 3],
                 position: List[str] = ['a', 'a', 'a'],
                 reflector: str = 'b'):

        assert (len(rotors) == len(position))
        assert (len(rotors) <= 8)

        self.position = position  # current rotor position
        self.basic_position = position.copy()  # for config restart
        self.rotors = [r - 1 for r in rotors]  # convert to base 0
        self.reflector = ord(reflector) - ord('b')
        assert (self.reflector >= 0 and self.reflector <= 1)
        # data from wikipedia, https://en.wikipedia.org/wiki/Enigma_rotor_details#Rotor_wiring_tables
        self.rotor_list = [
            'ekmflgdqvzntowyhxuspaibrcj', 'ajdksiruxblhwtmcqgznpyfvoe',
            'bdfhjlcprtxvznyeiwgakmusqo', 'esovpzjayquirhxlnftgkdcmwb',
            'vzbrgityupsdnhlxawmjqofeck', 'jpgvoumfyqbenhzrdkasxlictw',
            'nzjhgrcxmyswboufaivlpekqdt', 'fkqhtlxocbjspdzramewniuygv'
        ]
        self.inverse_rotor_list = [
            'uwygadfpvzbeckmthxslrinqoj', 'ajpczwrlfbdkotyuqgenhxmivs',
            'tagbpcsdqeufvnzhyixjwlrkom', 'hzwvartnlgupxqcejmbskdyoif',
            'qcylxwenftzosmvjudkgiarphb', 'skxqlhcnwarvgmebjptyfdzuio',
            'qmgyvpedrcwtianuxfkzoslhjb', 'qjinsaydvkbfruhmcplewztgxo'
        ]
        self.rotor_notch = [('q', ), ('e', ), ('v', ), ('j', ), ('a', ),
                            ('z', 'm'), ('z', 'm'), ('z', 'm')]
        self.reflector_list = [
            'yruhqsldpxngokmiebfzcwvjat', 'fvpjiaoyedrzxwgctkuqsbnmhl'
        ]

    def reset(self):
        self.position = self.basic_position

    def _rotor_wiring_(self, char: str, key: str, diff: int):
        wired_char = self._translate_(char, key, diff)
        return self._translate_(wired_char, diff=-diff)

    def _translate_(self,
                    char: str,
                    rotor_key: str = 'abcdefghijklmnopqrstuvwxyz',
                    diff: int = 0):
        idx = (Base.str_to_list_int(char)[0] + diff) % 26
        return rotor_key[idx]

    def _turn_rotor_(self):
        if self.position[1] in self.rotor_notch[self.rotors[1]]:
            # double step
            self.position[0] = self._translate_(self.position[0], diff=1)
            self.position[1] = self._translate_(self.position[1], diff=1)

        if self.position[2] in self.rotor_notch[self.rotors[2]]:
            # single step
            self.position[1] = self._translate_(self.position[1], diff=1)
        # normal step
        self.position[2] = self._translate_(self.position[2], diff=1)

    def _reflect_(self, char: str) -> str:
        return self._translate_(char, self.reflector_list[self.reflector])

    def _encrypt_one_(self, char):
        self._turn_rotor_()
        # print('pos:', self.position)
        encrypted = char
        # translate from right to left
        for rotor_idx in range(len(self.rotors) - 1, -1, -1):
            diff = Base.str_to_list_int(self.position[rotor_idx])[0]
            encrypted = self._rotor_wiring_(
                encrypted, self.rotor_list[self.rotors[rotor_idx]], diff)
            # print(f'w{rotor_idx}:', encrypted)
        encrypted = self._reflect_(encrypted)
        # print('r:', encrypted)
        # translate from left to right
        for rotor_idx in range(len(self.rotors)):
            diff = Base.str_to_list_int(self.position[rotor_idx])[0]
            encrypted = self._rotor_wiring_(
                encrypted, self.inverse_rotor_list[self.rotors[rotor_idx]],
                diff)
            # print(f'w{rotor_idx}:', encrypted)

        return encrypted

    def encrypt(self, plain_text: str, *args, **kwargs) -> str:
        encrypted = ''
        for char in plain_text:
            if char.isalpha():
                encrypted += self._encrypt_one_(char)
                # print(encrypted)
            else:
                encrypted += char

        return encrypted

    def decrypt(self, cipher_text: str, *args, **kwargs) -> str:
        return self.encrypt(cipher_text, *args, **kwargs)

    def render(self, window: Ui_MainWindow):
        self.groupBox_15 = QtWidgets.QGroupBox(window.cipherWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_15.sizePolicy().hasHeightForWidth())
        self.groupBox_15.setSizePolicy(sizePolicy)
        self.groupBox_15.setMaximumSize(QtCore.QSize(160, 16777215))
        self.groupBox_15.setObjectName("groupBox_15")
        self.formLayout_11 = QtWidgets.QFormLayout(self.groupBox_15)
        self.formLayout_11.setObjectName("formLayout_11")
        self.label_21 = QtWidgets.QLabel(self.groupBox_15)
        self.label_21.setMinimumSize(QtCore.QSize(50, 0))
        self.label_21.setObjectName("label_21")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.comboBox_16 = QtWidgets.QComboBox(self.groupBox_15)
        self.comboBox_16.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox_16.setMaximumSize(QtCore.QSize(16777215, 25))
        self.comboBox_16.setObjectName("comboBox_16")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_16)
        self.label_22 = QtWidgets.QLabel(self.groupBox_15)
        self.label_22.setObjectName("label_22")
        self.formLayout_11.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_15)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_11.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.formLayout_11.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)
        window.verticalLayout_4.addWidget(self.groupBox_15)
        self.groupBox_16 = QtWidgets.QGroupBox(window.cipherWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_16.sizePolicy().hasHeightForWidth())
        self.groupBox_16.setSizePolicy(sizePolicy)
        self.groupBox_16.setMaximumSize(QtCore.QSize(160, 16777215))
        self.groupBox_16.setObjectName("groupBox_16")
        self.formLayout_12 = QtWidgets.QFormLayout(self.groupBox_16)
        self.formLayout_12.setObjectName("formLayout_12")
        self.label_23 = QtWidgets.QLabel(self.groupBox_16)
        self.label_23.setMinimumSize(QtCore.QSize(50, 0))
        self.label_23.setObjectName("label_23")
        self.formLayout_12.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.comboBox_17 = QtWidgets.QComboBox(self.groupBox_16)
        self.comboBox_17.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox_17.setMaximumSize(QtCore.QSize(16777215, 25))
        self.comboBox_17.setObjectName("comboBox_17")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.formLayout_12.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_17)
        self.label_24 = QtWidgets.QLabel(self.groupBox_16)
        self.label_24.setObjectName("label_24")
        self.formLayout_12.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_16)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_12.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.formLayout_12.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_12)
        window.verticalLayout_4.addWidget(self.groupBox_16)
        self.groupBox_17 = QtWidgets.QGroupBox(window.cipherWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_17.sizePolicy().hasHeightForWidth())
        self.groupBox_17.setSizePolicy(sizePolicy)
        self.groupBox_17.setMaximumSize(QtCore.QSize(160, 16777215))
        self.groupBox_17.setObjectName("groupBox_17")
        self.formLayout_13 = QtWidgets.QFormLayout(self.groupBox_17)
        self.formLayout_13.setObjectName("formLayout_13")
        self.label_25 = QtWidgets.QLabel(self.groupBox_17)
        self.label_25.setMinimumSize(QtCore.QSize(50, 0))
        self.label_25.setObjectName("label_25")
        self.formLayout_13.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.comboBox_18 = QtWidgets.QComboBox(self.groupBox_17)
        self.comboBox_18.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox_18.setMaximumSize(QtCore.QSize(16777215, 25))
        self.comboBox_18.setObjectName("comboBox_18")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.formLayout_13.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_18)
        self.label_26 = QtWidgets.QLabel(self.groupBox_17)
        self.label_26.setObjectName("label_26")
        self.formLayout_13.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_17)
        self.lineEdit_13.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_13.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.formLayout_13.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_13)
        window.verticalLayout_4.addWidget(self.groupBox_17)
        self.groupBox_18 = QtWidgets.QGroupBox(window.cipherWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_18.sizePolicy().hasHeightForWidth())
        self.groupBox_18.setSizePolicy(sizePolicy)
        self.groupBox_18.setObjectName("groupBox_18")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_18)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.comboBox_19 = QtWidgets.QComboBox(self.groupBox_18)
        self.comboBox_19.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox_19.setMaximumSize(QtCore.QSize(16777215, 25))
        self.comboBox_19.setObjectName("comboBox_19")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_19)
        window.verticalLayout_4.addWidget(self.groupBox_18)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        # Form.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_15.setTitle(_translate("MainWindow", "Rotor 1"))
        self.label_21.setText(_translate("MainWindow", "Type"))
        self.comboBox_16.setItemText(0, _translate("MainWindow", "I"))
        self.comboBox_16.setItemText(1, _translate("MainWindow", "II"))
        self.comboBox_16.setItemText(2, _translate("MainWindow", "III"))
        self.comboBox_16.setItemText(3, _translate("MainWindow", "IV"))
        self.comboBox_16.setItemText(4, _translate("MainWindow", "V"))
        self.comboBox_16.setItemText(5, _translate("MainWindow", "VI"))
        self.comboBox_16.setItemText(6, _translate("MainWindow", "VII"))
        self.comboBox_16.setItemText(7, _translate("MainWindow", "VIII"))
        self.label_22.setText(_translate("MainWindow", "Key"))
        self.groupBox_16.setTitle(_translate("MainWindow", "Rotor 2"))
        self.label_23.setText(_translate("MainWindow", "Type"))
        self.comboBox_17.setItemText(0, _translate("MainWindow", "I"))
        self.comboBox_17.setItemText(1, _translate("MainWindow", "II"))
        self.comboBox_17.setItemText(2, _translate("MainWindow", "III"))
        self.comboBox_17.setItemText(3, _translate("MainWindow", "IV"))
        self.comboBox_17.setItemText(4, _translate("MainWindow", "V"))
        self.comboBox_17.setItemText(5, _translate("MainWindow", "VI"))
        self.comboBox_17.setItemText(6, _translate("MainWindow", "VII"))
        self.comboBox_17.setItemText(7, _translate("MainWindow", "VIII"))
        self.label_24.setText(_translate("MainWindow", "Key"))
        self.groupBox_17.setTitle(_translate("MainWindow", "Rotor 3"))
        self.label_25.setText(_translate("MainWindow", "Type"))
        self.comboBox_18.setItemText(0, _translate("MainWindow", "I"))
        self.comboBox_18.setItemText(1, _translate("MainWindow", "II"))
        self.comboBox_18.setItemText(2, _translate("MainWindow", "III"))
        self.comboBox_18.setItemText(3, _translate("MainWindow", "IV"))
        self.comboBox_18.setItemText(4, _translate("MainWindow", "V"))
        self.comboBox_18.setItemText(5, _translate("MainWindow", "VI"))
        self.comboBox_18.setItemText(6, _translate("MainWindow", "VII"))
        self.comboBox_18.setItemText(7, _translate("MainWindow", "VIII"))
        self.label_26.setText(_translate("MainWindow", "Key"))
        self.groupBox_18.setTitle(_translate("MainWindow", "Reflector"))
        self.comboBox_19.setItemText(0, _translate("MainWindow", "UKW B"))
        self.comboBox_19.setItemText(1, _translate("MainWindow", "UKW C"))