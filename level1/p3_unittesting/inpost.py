import unittest

"""
InPost
Dane są: rozmiary szafek w paczkomacie, np. 
[2,4,8,8,2]
oraz rozmiary paczek, np.
[1,5,1,3]
Pytanie: czy jest możliwość umieszczenia wszystkich paczek w paczkomacie, tak by każda paczka
znalazła się w skrzynce conajmniej tej wielkości, jakiej sama wymaga. 
Zwracamy z funkcji: 
True    # jeśli da się umieścić paczki, lub
False   # w przeciwnym przypadku
"""


def inpost(szafki, paczki):
    if len(szafki) >= len(paczki):
        for i in range(len(paczki)):
            naj_paczka = max(paczki)
            naj_szafka = max(szafki)
            if naj_paczka > naj_szafka:
                return False
            szafki.remove(naj_szafka)
            paczki.remove(naj_paczka)
    else:
        return False
    return True


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(inpost([1, 1, 1, 1], [1, 1, 1]), True, 'Więcej szafek niż paczek')

    def test_2(self):
        self.assertEqual(inpost([1, 1], [1, 1, 1]), False, 'Więcej paczek niż szafek')

    def test_3(self):
        self.assertEqual(inpost([10], [5]), True, 'Duża szafka...')

    def test_4(self):
        self.assertEqual(inpost([5], [10]), False, 'Za duża paczka...')

    def test_5(self):
        self.assertEqual(inpost([2, 2, 2, 2], [1, 1, 3]), False, 'Znowu za duża paczka...')

    def test_6(self):
        self.assertEqual(inpost([2, 4, 8, 8, 2], [1, 3, 5, 3]), True, 'Kilka ciekawych paczek i skrzynek')

    def test_7(self):
        self.assertEqual(inpost([2, 4, 8, 8, 2], [5, 3, 5, 6]), False, 'Tu chyba nie ma szans...')
    def test_8(self):
        self.assertEqual(inpost([1]*20000, [1]*20000), True, 'Powinno przejsc, liczenie ')


if __name__ == '__main__':
    unittest.main()