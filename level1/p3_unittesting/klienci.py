import unittest

w = [4,6,9,1,10,5,8,30,4,2,1]

def ile_w_30min(tab):
    najwiekszy = tab[1] + tab[2] + tab[3] #dla uproszczenia zakladamy ze ma min 30 min
    for i in range(len(tab)):
        if i < len(tab)-3:
            temp = tab[i]+tab[i+1]+tab[i+2]
            najwiekszy = temp if temp > najwiekszy else najwiekszy
    return najwiekszy

class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(ile_w_30min([1, 1, 1, 1]), 3, 'Dla listy jedynek -- po prostu 3')

    def test_2(self):
        self.assertEqual(ile_w_30min([1, 0, 0, 1]), 1, 'Pojedynczy klienci')

    def test_3(self):
        self.assertEqual(ile_w_30min([4, 6, 9, 1, 10, 5, 8, 30, 4, 2, 1]), 43, 'Realistyczny przykład')

    def test_4(self):
        self.assertEqual(ile_w_30min([1] * 100000), 3, 'Długa lista')


if __name__ == '__main__':
    unittest.main().main()
