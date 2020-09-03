from cipher import *


def test_vigenere_basic():
    c = Vigenere()
    c.set_matrix(26)
    c.key = 'sony'
    plain = c.encrypt('thisplaintext')

    assert (plain == 'lvvqhzngfhrvl')
    assert (c.decrypt(plain) == 'thisplaintext')
