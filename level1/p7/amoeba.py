import unittest
from typing import List

"""
Amoeba pożera bakterie różnej wielkości, rosnąc przy każdym posiłku o wielkość tego co zjdała. 
Formalnie amoeba ma na początku wielkość X, i może zjeść wyłącznie bakterię wielkości X, powiększając
się do wielkości 2*X. Czynność tą powtaża póki można znaleźć pokarm odpowiedniej wielkości. Jeśli
w pewnej chwili nie ma bakterii o wielkości X, to amoeba przestaje rosnąć i nic już nie zje. 
Mając daną początkową wielkość amoeby i wielkości bakterii w jej okolicy, podać końcową wielkość amoeby. 
"""


def amoeba(x: int, bacteria: List[int]):
    bacteria.sort()
    print(bacteria)
    for i in bacteria:
        if x == i:
            x += i
        elif x < i:
            return x
    return x


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(amoeba(1, [1, 1, 2, 8, 4]), 16, '')

    def test_2(self):
        self.assertEqual(amoeba(1, [2, 2, 2, 4, 4]), 1, '')

    def test_3(self):
        self.assertEqual(amoeba(2, [1, 1, 2, 8, 4]), 16, '')

    def test_4(self):
        self.assertEqual(amoeba(2, [2, 2, 2, 4, 4]), 8, '')

    def test_5(self):
        self.assertEqual(amoeba(1, [1, 1]), 2, '')

    def test_6(self):
        self.assertEqual(amoeba(7, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), 28, '')


if __name__ == '__main__':
    unittest.main()