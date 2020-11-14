import unittest
from typing import List

"""
Dana jest kwadratowa tablica 2-wymiarowa np. [[1, 2, 3], [2, 3, 4], [1, 2, 3]]. 
Sprawdzić czy suma każdego z rzędów i każdej z kolumn jest równa (wszystkie te liczby są równe).

"""

def sudoku(tab: List):
    goal = sum(tab[0])

    for i in tab:
        if sum(i) != goal:
            return False
    n = len(tab)
    for c in range(n):
        suma = 0
        for g in range(n):
            suma += tab[g][c]
        if suma != goal:
            return False
    return True





class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(sudoku([[1, 1], [1, 1]]), True, '')

    def test_2(self):
        self.assertEqual(sudoku([[1, 2], [1, 2]]), False, '')

    def test_3(self):
        self.assertEqual(sudoku([[1, 1], [2, 2]]), False, '')

    def test_3x(self):
        self.assertEqual(sudoku([[1, 1, 1], [1, 1, 1], [2, 2, 2]]), False, '')

    def test_4(self):
        w = [[1 for i in range(10)] for _ in range(10)]
        self.assertEqual(sudoku(w), True, '')

    def test_5(self):
        w = [[1 for i in range(10)] for _ in range(10)]
        w[0][0] = 2
        self.assertEqual(sudoku(w), False, '')




if __name__ == '__main__':
    unittest.main()