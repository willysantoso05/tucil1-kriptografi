from .base import Base

NUMBER_OF_ALPHABET = 26

class Affine:
    def __init__(self, key_m: int, key_b: int):
        self.key_m = key_m
        self.key_b = key_b

    def encrypt(self, plain_text: str, *args, **kwargs) -> str:
        list_int_plain_text = Base.str_to_list_int(plain_text, *args, **kwargs)
        list_int_cipher_text = []

        for i in range(len(list_int_plain_text)):
            list_int_cipher_text.append((list_int_plain_text[i] * self.key_m + self.key_b) % NUMBER_OF_ALPHABET)
        
        return Base.list_int_to_str(list_int_cipher_text, *args, **kwargs)

    def decrypt(self, cipher_text: str, *args, **kwargs) -> str:
        list_int_cipher_text = Base.str_to_list_int(cipher_text, *args, **kwargs)
        list_int_plain_text = []
        
        m_inverse = Base.modInverse(self.key_m, NUMBER_OF_ALPHABET)

        for i in range(len(list_int_cipher_text)):
            list_int_plain_text.append((m_inverse * (list_int_cipher_text[i] - self.key_b)) % NUMBER_OF_ALPHABET)
        
        return Base.list_int_to_str(list_int_plain_text, *args, **kwargs)
