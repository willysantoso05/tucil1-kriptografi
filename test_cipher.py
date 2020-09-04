from cipher import *


def test_vigenere_basic():
    key = 'sony'
    c = Vigenere(key)
    c.set_matrix(26)
    plain_text = 'thisplaintext'
    cipher = c.encrypt(plain_text)
    cipher_text = 'lvvqhzngfhrvl'
    assert (cipher == cipher_text)
    deciphered_text = 'thisplaintext'
    assert (c.decrypt(cipher) == deciphered_text)


def test_affine_basic():
    c = Affine(7, 10)
    plain = c.encrypt('kripto')

    assert (plain == 'czolne')
    assert (c.decrypt(plain) == 'kripto')


def test_hill_basic():
    c = Hill('rrfvsvcct', 3)
    plain = c.encrypt('paymoremoney')

    assert (plain == 'lnshdlewmtrw')
    assert (c.decrypt(plain) == 'paymoremoney')


def test_playfair():
    key = 'jalan ganesha sepuluh'
    c = Playfair(key)
    plain_text = 'temui ibu nanti malam'
    cipher = c.encrypt(plain_text)
    cipher_text = 'zbrsfykupglgrkvsnlqv'
    assert (cipher == cipher_text)
    deciphered_text = 'temuixibunantimalamx'
    assert (c.decrypt(cipher) == deciphered_text)
