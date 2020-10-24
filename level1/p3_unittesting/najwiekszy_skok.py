import unittest


# [1,2,8,2,6]
# Mając daną listę >=2 elementów wyznaczyć najwięszą wartość w[i+1]/w[i]...

def max_skok(lista):
    maks_skok = 0
    for i in range(len(lista)-1):
        if ((lista[i+1])/lista[i]) > maks_skok:
           maks_skok = (lista[i+1])/lista[i]
        else:
            continue

    print(maks_skok)
    return maks_skok

# rozwiazanie nauczyciela
def max_skok2(lista):
    best = lista[1]/lista[0]
    for i in range(len(lista)-1):
        best = max(best, lista[i+1]/lista[i])
    return best


def max_skok3(lista):
    max = 0
    for w in range(len(lista)-1):
        if (lista[w+1]/lista[w]) > max:
            max = lista[w+1]/lista[w]
    print(max)
    return max

class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(max_skok([1, 1, 1, 1]), 1, 'Dla listy stałej -- 1')

    def test_2(self):
        self.assertEqual(max_skok([1, 2]), 2, 'Prosty przypadek -- skok dwukrotny')

    def test_3(self):
        self.assertEqual(max_skok([1, 2, 6, 60]), 10, 'Ostatni duży skok')

    def test_4(self):
        self.assertEqual(max_skok3([8, 4, 0.1, 0.00000001]), 1 / 2, 'Lista malejąca')

    def test_5(self):
        self.assertEqual(max_skok([16, 8, 4, 2, 1, 2, 4, 8, 16]), 2, 'Lista malejąco rosnąca')

    def test_6(self):
        self.assertEqual(max_skok([1, 1, 1, 1.0000000000000000000000000000000001]),
                         1.0000000000000000000000000000000001, 'Bardzo mały przyrost')


if __name__ == '__main__':
    unittest.main()