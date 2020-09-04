from .base import Base


class Enigma(Base):
    def encrypt(self, plain_text, *args, **kwargs):
        return super().encrypt(plain_text, *args, **kwargs)

    def decrypt(self, cipher_text, *args, **kwargs):
        return super().decrypt(cipher_text, *args, **kwargs)