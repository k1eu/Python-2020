"""
Zadanie A:
Dane są dwie liczby: (a,b), a<b<10**6;
startujemy od liczby `a`;
w jednym kroku można dodać do niej 1, lub pomnożyć ją przez 2.
Wyznaczyć po ilu krokach minimalnie można osiągnąć liczbę `b`.

"""

import unittest
import random

def wynik(a,b):
    if b == 0 or a == b or b < a:
        return 0
    index = 0
    roznica = b - a

    while a != b:
        if a*2 <= b and a != 0:
            a *= 2
            index += 1
        else:
            a += 1
            index += 1
    return index


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(wynik(1, 4), 2, 'Pierwszy')

    def test_2(self):
        self.assertEqual(wynik(6, 28), 3, 'Drugi')

    def test_3(self):
        self.assertEqual(wynik(5, 5), 0, 'Trzeci')

    def test_4(self):
        self.assertEqual(wynik(1, 11), 5, 'Czwarty')

    def test_5(self):
        self.assertEqual(wynik(0, 12), 5, 'Piąty')

    def test_6(self):
        self.assertEqual(wynik(12, 0), 0, 'Szósty')

    def test_rnd1(self):
        random.seed(111)
        a = []
        b = []
        for i in range(10):
            r = random.randint(1, 1000)
            a.append(r)
            b.append(r + random.randint(1000, 10000))

        res = [wynik(aa, bb) for (aa, bb) in zip(a, b)]
        self.assertEqual(res, [488, 838, 85, 114, 474, 562, 368, 97, 93, 61], '¯\_(ツ)_/¯')


if __name__ == '__main__':
    unittest.main()