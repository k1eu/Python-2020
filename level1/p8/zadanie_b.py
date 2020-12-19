"""
Zadanie B:
Dany jest zbiór nominałów monet, np. (1,2,5,10) lub (2,7,9), oraz kwota X.
Wyznaczyć _jakiś_ sposób rozmienienia X na podane nominały, lub napisać że to nie możliwe.
"""
def test(nominaly,x):
    s = set()
    for i in nominaly:
        s.add(i)
