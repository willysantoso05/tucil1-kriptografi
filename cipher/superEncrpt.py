import numpy as np
import itertools
from .base import Base
from .vigenere import Vigenere

DEFAULT_NUM_ALPHABET = 26

class SuperEncrypt(Vigenere):
    def __init__(self, key: str):
        super().__init__(key)
        super().set_matrix(DEFAULT_NUM_ALPHABET)

    def encrypt(self, plain_text: str, k_transpose: int, *args, **kwargs) -> str:
        x = len(plain_text) % k_transpose
        if(x != 0):
            plain_text += (k_transpose - x) * 'z'   #add Z character
        
        vigenere_text = super().encrypt(plain_text)
        return SuperEncrypt.transpose(vigenere_text, k_transpose)


    def decrypt(self, cipher_text: str, k_transpose: int, *args, **kwargs) -> str:
        transpose_text = SuperEncrypt.transpose(cipher_text, k_transpose)
        cipher_text = super().decrypt(transpose_text)
        return cipher_text

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
