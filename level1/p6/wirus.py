import unittest
from typing import List
from random import randint, seed

"""
Kod genetyczny wirusa zapisano w postaci napisu, np. `vir = 'GGGAAYYYYVVYY'`. 
Wiadomo, że wirus nie uległ mutacji jeśli `g` składa się _wyłącznie_ 
z kawałków podanej listy, np. `genes=['GGG','AA','Y','VV']`. 
Sprawdzić czy `vir` zawiera mutacje (tak/nie). 
[Odpowiedź: True znaczy, że wirus zawiera mutacje, czyli nie da się go ułożyć z elementów `genes`]
[Uwaga: Elementy tablicy `genes` nie zawierają wspólnych liter.]
"""

# TODO DOKONCZYC BO NIE DZIALA
def wirus(vir: str, genes: List[str]):
    conti = True
    while len(vir) > 0:
        for i in genes:
            if vir.startswith(i):
                l = len(i)
                vir = vir[l:]
                if len(vir) < 1:
                    return False



"""
lenvir 3
3
    G
    1
    GA
    

"""




class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(wirus('GGA', ['G', 'A']), False, '')

    def test_2(self):
        self.assertEqual(wirus('GAG', ['GG', 'A']), True, '')

    def test_3(self):
        self.assertEqual(wirus('AABBCCDD', ['AA', 'BB', 'CC', 'DD']), False, '')

    def test_4(self):
        self.assertEqual(wirus('AABBCCCDD', ['AA', 'BB', 'CC', 'DD']), True, '')

    def test_5(self):
        self.assertEqual(wirus('AAABCA', ['A', 'BC']), False, '')


if __name__ == '__main__':
    unittest.main()