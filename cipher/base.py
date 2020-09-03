import re
from typing import List, Union


class Base:
    def __init__(self, key: str):
        self.key = key

    def encrypt(self, plain_text: str, *args, **kwargs) -> str:
        return plain_text

    def decrypt(self, cipher_text: str, *args, **kwargs) -> str:
        return cipher_text

    @staticmethod
    def str_to_list_int(
        text: Union[str, List[str]], base: int = ord('a')) -> List[int]:
        '''Convert str to list of int
        
        Convertion done by substract each char by base,
        so the smallest char will have int = 0
        '''
        return [(ord(char) - base) for char in text]

    @staticmethod
    def list_int_to_str(list_int: List[int], base: int = ord('a')) -> str:
        '''Convert list of int to str

        Convertion done by adding each num with base,
        so the number 0 will have char = chr(base)
        '''
        return ''.join([chr(num + base) for num in list_int])

    @staticmethod
    def remove_punctuation(text: str, filter: str = '[^a-zA-Z]') -> str:
        return re.sub(filter, '', text)
