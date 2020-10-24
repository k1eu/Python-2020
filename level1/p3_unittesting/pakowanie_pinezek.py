import unittest


# w każdym opakowaniu zmieści się co najwyżej `pinezek_w_opakowaniu` pinezek...
# ile opakowań potrzeba by zmieścić wszystkie `liczba_pinezek`

# liczba_pinezek > 0, pinezek_w_opakowaniu > 0; obie są liczbami całkowitymi

def ile_opakowan(liczba_pinezek, pinezek_w_opakowaniu):
    wynik = 1
    if liczba_pinezek <= pinezek_w_opakowaniu:
        return wynik
    else:
        wynik = liczba_pinezek // pinezek_w_opakowaniu
        wynik += 1 if (liczba_pinezek % pinezek_w_opakowaniu) != 0 else 0
        return wynik
# rozw nauczyciela

def ile_opakowan2(liczba_pinezek, pinezek_w_opakowaniu):
    full = liczba_pinezek // pinezek_w_opakowaniu
    answer = full
    if full * pinezek_w_opakowaniu < liczba_pinezek:
        # jakieś zostały
        answer += 1
    return answer

class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(ile_opakowan(10, 100), 1, 'Mało pinezek, duże opakowanie -- ez; wystarczy 1')

    def test_2(self):
        self.assertEqual(ile_opakowan(10, 10), 1, 'Wystarczy 1... ale będzie pełne')

    def test_3(self):
        self.assertEqual(ile_opakowan(505, 100), 6, 'W ostatnim będzie tylko 5/100 pinezek')

    def test_4(self):
        self.assertEqual(ile_opakowan(10**11, 10), 10**10, 'Dużo pinezek')




if __name__ == '__main__':
    unittest.main()