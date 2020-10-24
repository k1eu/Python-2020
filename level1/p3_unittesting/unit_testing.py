import unittest


# to jest funkcja którą będziemy testowali
def add(a, b):
    return a + b


def suma_listy(lista):
    sum = 0
    for i in lista:
        sum += i
    return sum


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(add(2, 2), 4, 'Dodawanie liczb dodatnich działa')

    def test_sum_neg(self):
        self.assertEqual(add(2, -2), 0, 'Dodawanie liczb ujemnych jest ok')

    def test_suma_listy_z_1_elementem(self):
        self.assertEqual(suma_listy([4]), 4, 'Suma listy 1-elementowej to ten element')

    def test_suma_listy_pustej(self):
        self.assertEqual(suma_listy([]), 0, 'Suma listy pustej to zero')

    def test_suma_listy_jedynek(self):
        lista = [1] * 100  # lista ze 100 elementów; każdy = 1
        self.assertEqual(suma_listy(lista), len(lista), 'Suma listy jedynek jest długością listy')


if __name__ == '__main__':
    unittest.main()