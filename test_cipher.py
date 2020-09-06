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


def test_super_encrypt():
    key = 'sony'
    plain = 'thisisplaintext'
    k = 3

    c = SuperEncrypt(key)
    cipher = c.encrypt(plain, k)
    cipher_text = 'lqcwwvajalvgsrg'
    assert (cipher == cipher_text)
    assert (c.decrypt(cipher_text, int(len(plain) / k)) == plain)


def test_enigma():
    plain = 'en1, gm4aaaaa'

    c = Enigma(rotors=[1, 2, 3], position=['a', 'd', 'v'], reflector='b')
    cipher = c.encrypt(plain)
    cipher_text = 'bt1, qa4gfjbw'

    assert (cipher == cipher_text)
    c.reset()
    assert (c.decrypt(cipher) == plain)
