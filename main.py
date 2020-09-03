from cipher import *

if __name__ == "__main__":
    c: Base = globals().get('Vigenere')()

    c.set_matrix(26)

    c.key = 'sony'
    plain = c.encrypt('thisplaintext')
    assert (plain == 'lvvqhzngfhrvl')
    print(c.decrypt(plain))