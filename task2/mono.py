import random
__author__ = 'Timofey Khirianov'
# -*- coding: utf8 -*-


class Monoalphabet:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, keytable):
        assert sorted(list(keytable)) == sorted(list(self.alphabet)), \
               "Плохая кодовая таблица"
        lowercase_code = {x: y for x, y in zip(self.alphabet, keytable)}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, keytable)}
        self._encode = lowercase_code
        self._encode.update(uppercase_code)
        self._decode = {self._encode[x]:x for x in self._encode}

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, cifertext):
        return ''.join([self._decode.get(char, char) for char in cifertext])


#key = "ьзцвкбщхфпрялэаеышумъжёогйндитчюс"
#key = "щевыдхёжукйплрмастинзфбцчшоъяьэюг"
#key = "дбвгеиёжзлйкнмопрсутыфхцчшщъаьэюя"  # answer!
#key = "ыбвгадёжзейкимлнопртсфхцчшщъуьэюя"  #decode
#key = "ыбвгедёжзийкамлнопртсфхцчшщъуьэюя"  #part decode
"""alp = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
cipher = Monoalphabet(key)
line = input()
while line != '.':
    print(cipher.encode(line))
    line = input()
"""

key_tv = "онпгдуёжзийкаыблврфтесхцчшщъмьэюя"
cipher = Monoalphabet(key_tv)
text = """Не надо бояться густого тумана,
Не надо бояться пустого кармана.
Не надо бояться ни горных потоков,
Ни топей болотных, ни грязных подонков!
Не надо бояться тяжёлой задачи,
А надо бояться дешёвой удачи.
Не надо бояться быть честным и битым,
А надо бояться быть лживым и сытым!
Умейте всем страхам в лицо рассмеяться, —
Лишь собственной трусости надо бояться!"""
print(cipher.encode(text))
