import sys

from typing import Union


class kid_enigma:

    @classmethod
    def _alg(cls, text: str, /, multiplier: int = 1, direction: int = 1) -> str:

        def shift_index(x: int) -> int:
            shifted = (x + (word_pos * direction)) % sys.maxunicode
            # assert 0 <= shifted < length
            return shifted

        new_text = []

        for word_pos, word in enumerate(text.split(), start=multiplier):

            word_indices = list(map(shift_index, [ord(ltr) for ltr in word]))
            new_text.append(''.join([chr(i) for i in word_indices]))

        return (' '.join(new_text))

    @classmethod
    def crypt(cls, text: str, multiplier: int = 42) -> bytes:
        return cls._alg(text, multiplier=multiplier).encode('utf-8')

    @classmethod
    def decrypt(cls, text: Union[str, bytes], multiplier: int = 42) -> str:
        if isinstance(text, bytes):
            text = text.decode('utf-8')
        return cls._alg(text, direction=-1, multiplier=multiplier)


to_crypt = """Hello! This is my first message that I sent you with my new cryptographic machine.
It's very simple, but it works pretty well!"""
print(to_crypt, end='\n\n')

crypted = kid_enigma.crypt(to_crypt)
print(crypted.decode('utf-8'), end='\n\n')

decrypted = kid_enigma.decrypt(crypted.decode('utf-8'))
print(decrypted, end='\n\n')
