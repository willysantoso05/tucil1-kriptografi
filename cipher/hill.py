import numpy as np
import re
import random
import string

from .base import Base

NUMBER_OF_ALPHABET = 26

class Hill:
    def __init__(self, key: str, m_linear: int):
        self.key = key
        self.m_linear = m_linear

        self.processingKey()

    def encrypt(self, plain_text: str, *args, **kwargs) -> str:
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

    def processingKey(self):
        if(len(self.key) > self.m_linear * self.m_linear):
            self.key = self.key[0:self.m_linear * self.m_linear]
        elif(len(self.key) < self.m_linear * self.m_linear):
            self.key += str(''.join(random.choices(string.ascii_uppercase, k=self.m_linear * self.m_linear-len(self.key)))) 
