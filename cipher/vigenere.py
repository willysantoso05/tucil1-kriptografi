from itertools import cycle
from random import shuffle
from typing import List

from .base import Base
from utils import (str_to_list_int, list_int_to_str)


class Vigenere(Base):
    matrix = list()

    def encrypt(self, plain_text: str, *args, **kwargs) -> str:
        list_int_plain_text = str_to_list_int(plain_text, *args, **kwargs)

        list_int_key = str_to_list_int(self.key, *args, **kwargs)

        list_int_cipher_text = [
            self.matrix[key][num]
            for key, num in zip(cycle(list_int_key), list_int_plain_text)
        ]

        return list_int_to_str(list_int_cipher_text, *args, **kwargs)

    def decrypt(self, cipher_text: str, *args, **kwargs) -> str:

        list_int_cipher_text = str_to_list_int(cipher_text, *args, **kwargs)

        list_int_key = str_to_list_int(self.key, *args, **kwargs)

        list_int_plain_text = [
            self.matrix[key].index(num)
            for key, num in zip(cycle(list_int_key), list_int_cipher_text)
        ]

        return list_int_to_str(list_int_plain_text, *args, **kwargs)

    @staticmethod
    def generate_matrix(char_count: int,
                        shift: int = 1,
                        random: bool = False) -> List[List[int]]:
        '''Generate Vigenere Matrix

        if random is True then shift will not be used
        '''
        temp_matrix = list()
        for i in range(char_count):
            temp_row = [j for j in range(i, char_count + i)]
            if random:
                shuffle(temp_row)
            else:
                temp_row = [j % char_count for j in temp_row]
            temp_matrix.append(temp_row)

        return temp_matrix

    def set_matrix(self, *args, **kwargs):
        '''Set self.matrix with Vigenere.generate_matrix()
        '''
        self.matrix = Vigenere.generate_matrix(*args, **kwargs)
