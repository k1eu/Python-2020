import unittest
from typing import List

"""
Mamy podany rozkład siedzeń w pojedynczym rzędzie w kinie w postaci pojedynczego napisu (string). 
Napis zawiera wyłącznie literki 'R' lub 'L', gdzie 'R' oznacza, że siedzący na danym miejscu
widz kładzie swój łokieć na poręczy siedzenia po swojej prawej stronie, a 'L', że widz kładzie
łokieć na poręczy po swojej lewej stronie. Wiadomo, że jeśli sąsiedni widzowe kładą łokcie
na tej samej poręczy, to nastąpi _konflikt_ (czyli np. w sytuacji 'RL', ale nie w 'RR', czy 'LR'). 
Policzyć ile konfliktów powstanie w danym rzędzie. 
"""


def elbows(row):
    conflict_app = 0
    lngth = len(row)
    for i in range(lngth):
        if i < lngth-1:
            if row[i] + row[i+1] == 'RL':
                conflict_app += 1
    return conflict_app


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(elbows('LLL'), 0, '')

    def test_2(self):
        self.assertEqual(elbows('LRL'), 1, '')

    def test_3(self):
        self.assertEqual(elbows('R'), 0, '')

    def test_4(self):
        self.assertEqual(elbows('RRRRLLLLLLLLLRR'), 1, '')

    def test_5(self):
        self.assertEqual(elbows('RLRLRL'), 3, '')

    def test_6(self):
        self.assertEqual(elbows('LLLLLLLRRRRRRRRRRRR'), 0, '')




if __name__ == '__main__':
    unittest.main()