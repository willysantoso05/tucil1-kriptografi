from cipher import *


def test_vigenere_basic():
    c = Vigenere('sony')
    c.set_matrix(26)
    plain = c.encrypt('thisplaintext')

    assert (plain == 'lvvqhzngfhrvl')
    assert (c.decrypt(plain) == 'thisplaintext')
