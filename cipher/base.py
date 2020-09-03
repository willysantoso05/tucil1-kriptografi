class Base:
    class NoKeyException(Exception):
        pass

    key = ''

    def encrypt(self, *args, **kwargs):
        pass

    def decrypt(self, *args, **kwargs):
        pass