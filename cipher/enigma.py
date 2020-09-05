from typing import List

from .base import Base


class Enigma(Base):
    '''Enigma M3 cipher without ring position and plug board.
    
    :param rotors: The rotors and their order. There are 8 rotors. e.g. [3,2,1]. 
    :param position: Rotor's start positions, consists of 3 alphabet e.g. ['C','Y','P']
    :param reflector: The reflector in use, B' or 'C'
    '''
    def __init__(self,
                 rotors: List[int] = [1, 2, 3],
                 position: List[str] = ['a', 'a', 'a'],
                 reflector: str = 'b'):

        assert (len(rotors) == len(position))
        assert (len(rotors) <= 8)

        self.position = position  # current rotor position
        self.basic_position = position.copy()  # for config restart
        self.rotors = [r - 1 for r in rotors]  # convert to base 0
        self.reflector = ord(reflector) - ord('b')
        assert (self.reflector >= 0 and self.reflector <= 1)
        # data from wikipedia, https://en.wikipedia.org/wiki/Enigma_rotor_details#Rotor_wiring_tables
        self.rotor_list = [
            'ekmflgdqvzntowyhxuspaibrcj', 'ajdksiruxblhwtmcqgznpyfvoe',
            'bdfhjlcprtxvznyeiwgakmusqo', 'esovpzjayquirhxlnftgkdcmwb',
            'vzbrgityupsdnhlxawmjqofeck', 'jpgvoumfyqbenhzrdkasxlictw',
            'nzjhgrcxmyswboufaivlpekqdt', 'fkqhtlxocbjspdzramewniuygv'
        ]
        self.inverse_rotor_list = [
            'uwygadfpvzbeckmthxslrinqoj', 'ajpczwrlfbdkotyuqgenhxmivs',
            'tagbpcsdqeufvnzhyixjwlrkom', 'hzwvartnlgupxqcejmbskdyoif',
            'qcylxwenftzosmvjudkgiarphb', 'skxqlhcnwarvgmebjptyfdzuio',
            'qmgyvpedrcwtianuxfkzoslhjb', 'qjinsaydvkbfruhmcplewztgxo'
        ]
        self.rotor_notch = [('q', ), ('e', ), ('v', ), ('j', ), ('a', ),
                            ('z', 'm'), ('z', 'm'), ('z', 'm')]
        self.reflector_list = [
            'yruhqsldpxngokmiebfzcwvjat', 'fvpjiaoyedrzxwgctkuqsbnmhl'
        ]

    def reset(self):
        self.position = self.basic_position

    def _rotor_wiring_(self, char: str, key: str, diff: int):
        wired_char = self._translate_(char, key, diff)
        return self._translate_(wired_char, diff=-diff)

    def _translate_(self,
                    char: str,
                    rotor_key: str = 'abcdefghijklmnopqrstuvwxyz',
                    diff: int = 0):
        idx = (Base.str_to_list_int(char)[0] + diff) % 26
        return rotor_key[idx]

    def _turn_rotor_(self):
        if self.position[1] in self.rotor_notch[self.rotors[1]]:
            # double step
            self.position[0] = self._translate_(self.position[0], diff=1)
            self.position[1] = self._translate_(self.position[1], diff=1)

        if self.position[2] in self.rotor_notch[self.rotors[2]]:
            # single step
            self.position[1] = self._translate_(self.position[1], diff=1)
        # normal step
        self.position[2] = self._translate_(self.position[2], diff=1)

    def _reflect_(self, char: str) -> str:
        return self._translate_(char, self.reflector_list[self.reflector])

    def _encrypt_one_(self, char):
        self._turn_rotor_()
        # print('pos:', self.position)
        encrypted = char
        # translate from right to left
        for rotor_idx in range(len(self.rotors) - 1, -1, -1):
            diff = Base.str_to_list_int(self.position[rotor_idx])[0]
            encrypted = self._rotor_wiring_(
                encrypted, self.rotor_list[self.rotors[rotor_idx]], diff)
            # print(f'w{rotor_idx}:', encrypted)
        encrypted = self._reflect_(encrypted)
        # print('r:', encrypted)
        # translate from left to right
        for rotor_idx in range(len(self.rotors)):
            diff = Base.str_to_list_int(self.position[rotor_idx])[0]
            encrypted = self._rotor_wiring_(
                encrypted, self.inverse_rotor_list[self.rotors[rotor_idx]],
                diff)
            # print(f'w{rotor_idx}:', encrypted)

        return encrypted

    def encrypt(self, plain_text: str, *args, **kwargs) -> str:
        encrypted = ''
        for char in plain_text:
            if char.isalpha():
                encrypted += self._encrypt_one_(char)
                # print(encrypted)
            else:
                encrypted += char

        return encrypted

    def decrypt(self, cipher_text: str, *args, **kwargs) -> str:
        return self.encrypt(cipher_text, *args, **kwargs)
