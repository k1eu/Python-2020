import unittest
from typing import List

"""
Dana jest tablica liczb, np. `w = [1,3,2,1,1]`. Lis Ciel startuje na pozycji 0, 
i będąc na pozycji `x` przechodzi  po minucie na pozycję `w[x]`. 
Sprawdzić czy Ciel wróci na pozycję 0 (po pewnym, możliwe że nawet długim, czasie). 
"""

def origin(w: List):
    index = 0
    for i in range(len(w)):
        index = w[index]
        if index == 0:
            return True
    return False

    return True


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(origin([1, 2, 3, 0]), True, '')

    def test_2(self):
        self.assertEqual(origin([1, 2, 3, 2]), False, '')

    def test_3(self):
        self.assertEqual(origin([0, 2, 2, 2, 2]), True, '')

    def test_4(self):
        self.assertEqual(origin([1, 0, 2, 3, 4]), True, '')

    def test_5(self):
        self.assertEqual(origin([4, 3, 2, 1, 0]), True, '')

    def test_6(self):
        self.assertEqual(origin([1, 2, 3, 2, 5, 4, 3, 2, 0]), False, '')


if __name__ == '__main__':
    unittest.main()