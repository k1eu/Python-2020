import unittest
from typing import List

"""
Tablica liczb jest "perfekcyjna" jeśli suma jej liczb jest podzielna przez jej długość. 
Np. [1,2,3] jest perfekcyjna, ale [1,1,1,2] nie jest. 
Mając daną tablicę zwiększyć - jeśli potrzeba - ostatnią liczbę minimalnie - 
tak by stała się perfekcyjna. Np. dla [1,1,1,2] wystarczy wziąć [1,1,1,5]. 
"""
from random import randint, seed


def perfect(tab: List):
    tablen = len(tab)
    suma = sum(tab)
    print(suma, tablen)
    if suma % tablen != 0:
        while suma % tablen != 0:
            suma += 1
            tab[-1] += 1
    return tab

class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(perfect([1]), [1], '')

    def test_2(self):
        self.assertEqual(perfect([1, 2]), [1, 3], '')

    def test_3(self):
        self.assertEqual(perfect([1, 5]), [1, 5], '')

    def test_4(self):
        self.assertEqual(perfect([3, 4]), [3, 5], '')

    def test_5(self):
        self.assertEqual(perfect([1, 1, 1, 1, 1, 1, 2]), [1, 1, 1, 1, 1, 1, 8], '')

    def test_6(self):
        seed(112)
        w = [randint(1, 18) for _ in range(20)]
        w[19] = 1
        ans = list(w)
        ans[19] = 13
        self.assertEqual(perfect(list(w)), ans, '')


if __name__ == '__main__':
    unittest.main()
