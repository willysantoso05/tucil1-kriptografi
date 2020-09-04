from collections import OrderedDict
from math import sqrt
import re

from .base import Base

DEFAULT_KEY = 'abcdefghiklmnopqrstuvwxyz'
DEFAULT_WIDTH = 5


class Playfair(Base):
    def __init__(self, key):
        super().__init__(key)
        self.key = Base.remove_punctuation(self.key)
        self.key = re.sub('j', '', self.key)
        self.key += DEFAULT_KEY
        self.key = ''.join(OrderedDict.fromkeys(self.key).keys())
        assert (len(self.key) == 25)

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
        plain_text = re.sub('j', 'i', plain_text)
        plain_text = Base.remove_punctuation(plain_text)

        for idx in range(1, len(plain_text), 2):
            # insert 'x' between same pair of char
            if (plain_text[idx] == plain_text[idx - 1]):
                plain_text = plain_text[:idx] + 'x' + plain_text[idx:]

        if len(plain_text) % 2 == 1:
            # text length in odd
            plain_text += 'x'

        return ''.join([
            self._encrypt_pair_(plain_text[idx], plain_text[idx + 1])
            for idx in range(0, len(plain_text), 2)
        ])

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
        cipher_text = re.sub('j', 'i', cipher_text)
        cipher_text = Base.remove_punctuation(cipher_text)

        if len(cipher_text) % 2 == 1:
            # text length in odd
            cipher_text += 'x'

        return ''.join([
            self._decrypt_pair_(cipher_text[idx], cipher_text[idx + 1])
            for idx in range(0, len(cipher_text), 2)
        ])