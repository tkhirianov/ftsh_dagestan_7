__author__ = 'Timofey Khirianov'
# -*- coding: utf8 -*-


class Vigenere:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, keyword):
        self._keyword = keyword
        self._alpha_index = {self.alphabet[i]:i for i in range(len(self.alphabet))}
        self._key = [self._alpha_index[letter] for letter in keyword]
        self._lower_alphabet = set(self.alphabet)
        self._upper_alphabet = set(self.alphabet.upper())

    def caesar(self, letter, shift):
        assert letter in self._lower_alphabet, "Expecting a lowercase russian letter"
        letter_index = self._alpha_index[letter]
        shifted_letter_index = (letter_index + shift)%len(self.alphabet)
        cifered_letter = self.alphabet[shifted_letter_index]
        return cifered_letter

    def encode(self, text):
        cifertext = []
        k = 0
        for letter in text:
            shift = self._key[k]
            if letter in self._lower_alphabet:
                cifered_letter = self.caesar(letter, shift)
            elif letter in self._upper_alphabet:
                cifered_letter = self.caesar(letter.lower(), shift).upper()
            else:
                cifered_letter = letter  # No cifering symbol not from alphabet
            cifertext.append(cifered_letter)
            k = (k + 1)%len(self._key)  # to use next letter of keyword
        return ''.join(cifertext)

    def decode(self, line):
        pass  # FIXME


keyword = input('Введите ключевое слово:')
cipher = Vigenere(keyword)
line = input()
while line != '.':
    print(cipher.encode(line))
    line = input()
