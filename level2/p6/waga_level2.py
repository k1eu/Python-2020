import itertools
import unittest
from random import randint, seed
from typing import List


def waga(coins: List[int]):
    n = len(coins)
    for a in itertools.product(range(2), repeat=n):
        left = []
        rght = []
        for i in range(n):
            if a[i] == 0:
                left.append(coins[i])
            else:
                rght.append(coins[i])
        if sum(left) == sum(rght):
            return True
    return False



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

    if sum(l) > half_sum:
        return False

    while not len(coins) < 1:
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
                    if i - j == l_sum - p_sum:
                        return True
    print(l)
    print(p)
    if sum(l) == sum(p):
        return True
    else:
        return False

def generate_equal_sum_lists():
    a = []
    b = []
    for _ in range(3):
        a.append(randint(1, 4))
        b.append(randint(1, 4))

    diff = sum(a) - sum(b)
    if diff > 0:
        b.append(diff)
    else:
        a.append(-diff)
    return a, b


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

    def test_7_mine(self):
        self.assertEqual(waga2([16, 8, 2]), False, '')

    def test_8_mine(self):
        self.assertEqual(waga2([4, 1, 4, 2, 2, 1, 1, 1]), True, '')

    def test_9_mine(self):
        self.assertEqual(waga2([130, 1, 120, 10, 1]), True, '')

    def test_10_mine(self):
        self.assertEqual(waga2([3, 6, 3, 1, 1]), True, '')

    def test_11_mine(self):
        self.assertEqual(waga2([1, 1]), True, '')

    def test_12_mine(self):
        self.assertEqual(waga2([16, 8, 8, 1]), False, '')

    def test_13_mine(self):
        self.assertEqual(waga2([1, 1, 1, 1]), True, '')

    def test_14_mine(self):
        self.assertEqual(waga2([1, 1, 3, 6, 44, 1000]), False, '')

    def test_15_mine(self):
        self.assertEqual(waga2([1, 1, 3]), False, '')

    def test_16_mine(self):
        self.assertEqual(waga2([10, 2, 2, 2, 1, 2, 2, 1]), True, '')

    def test_17_mine(self):
        self.assertEqual(waga2([2, 12, 10, 4]), True, '')

    def test_extra_1(self):
        self.assertEqual(waga2([7, 1, 3, 4, 5, 1, 1, 2, 4, 1, 1, 7, 1, 3, 5]), True, '')

    def test_extra_2(self):
        self.assertEqual(waga2([5, 2, 1, 2, 2, 3, 7, 6, 4, 8]), True, '')  # True w wersji 2 wynik 38/2 = 19

    def test_random(self):
        MAX = 100
        seed(111)
        for _ in range(MAX):
            a, b = generate_equal_sum_lists()
            a.extend(b)  # łączymy listy, ale wiemy, że rozwiązanie isnieje, bo sum(a) == sum(b)
            self.assertEqual(waga2(a), True, '')

if __name__ == '__main__':
    unittest.main()