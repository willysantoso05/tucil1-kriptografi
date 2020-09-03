from cipher import *


def test_vigenere_basic():
    c = Vigenere('sony')
    c.set_matrix(26)
    plain = c.encrypt('thisplaintext')

    assert (plain == 'lvvqhzngfhrvl')
    assert (c.decrypt(plain) == 'thisplaintext')

def test_affine_basic():
    c = Affine(7,10)
    plain = c.encrypt('kripto')

    assert(plain=='czolne')
    assert(c.decrypt(plain) == 'kripto')

def test_hill_basic():
    c = Hill('rrfvsvcct', 3)
    plain = c.encrypt('paymoremoney')

    assert(plain == 'lnshdlewmtrw')
    assert(c.decrypt(plain) == 'paymoremoney')