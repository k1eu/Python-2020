import unittest
from typing import List

def waga2(coins: List[int]):
    half_sum = sum(coins)/2

    if not half_sum.is_integer():
        return False

    highest = max(coins)
    l = [highest]
    p = []
    del coins[coins.index(highest)]

    if sum(l) == half_sum:
        return True

    while not sum(l) == sum(p):
        print(l)
        print(p)
        if len(coins) > 0:
            for i in coins:
                if sum(l) == half_sum:
                    p.extend(coins)
                    if sum(l) == sum(p):
                        return True
                    else:
                        return False
                    del coins
                elif sum(l) + i > half_sum:
                    p.append(i)
                    del coins[coins.index(i)]
                else:
                    l.append(i)
                    del coins[coins.index(i)]

        if sum(l) == sum(p):
            return True

        if len(coins) < 1:
            l_sum = sum(l)
            p_sum = sum(p)
            for i in l:
                for j in p:
                    if i - j == p_sum - l_sum and l.__contains__(i-j):
                        return True
    print(l)
    print(p)
    if sum(l) == sum(p):
        return True
    else:
        return False



class TestSum(unittest.TestCase):

    def test_x1(self):
        self.assertEqual(waga2([1, 1, 2]), True, '')

    def test_x2(self):
        self.assertEqual(waga2([1, 2, 3, 2]), True, '')  # True w wersji 2

    def test_x3(self):
        self.assertEqual(waga2([1, 1, 1]), False, '')

    def test_x4(self):
        self.assertEqual(waga2([1, 1, 1]), False, '')

    def test_x5(self):
        self.assertEqual(waga2([1, 1, 1, 1, 1, 1, 6]), True, '')

    def test_x6(self):
        self.assertEqual(waga2([2, 2, 3, 4, 5]), True, '')  # True w wersji 2


if __name__ == '__main__':
    unittest.main()