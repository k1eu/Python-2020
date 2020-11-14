import unittest
from typing import List
from random import randint, seed
import math

"""
Podana jest lista zabytkowych monet, każda oznaczona jedynie ich wagą. 
Monety trzeba podzielić na dwie grupy o równej (łącznej) wadze. Ocenić, czy da się to zrobić...
- wersja 1, prosta: poprzez wyznaczenie pozycji w liście tak, że elementy 
    na lewo od tej pozycji wchodzą do grupy1, a na prawo od niej (włącznie) do grupy 2. 
- wersja 2, trudniejsza: poprzez dowolny podział monet. 
[Uwaga: monet jest nie więcej niż 20.]
"""


def waga(coins: List[int]):
    suma = sum(coins)
    lewo = coins[:-1]
    prawo = [coins[-1]]
    if sum(lewo) == sum(prawo):
        return True
    else:
        for i in range(len(lewo)):
            x = lewo[-1]
            del lewo[-1]
            prawo.append(x)
            if sum(lewo) == sum(prawo):
                return True
        return False


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(waga([1, 1, 2]), True, '')

    def test_2(self):
        self.assertEqual(waga([1, 2, 3, 2]), False, '')  # True w wersji 2

    def test_3(self):
        self.assertEqual(waga([1, 1, 1]), False, '')

    def test_4(self):
        self.assertEqual(waga([1, 1, 1]), False, '')

    def test_5(self):
        self.assertEqual(waga([1, 1, 1, 1, 1, 1, 6]), True, '')

    def test_6(self):
        self.assertEqual(waga([2, 2, 3, 4, 5]), False, '')  # True w wersji 2


if __name__ == '__main__':
    unittest.main()