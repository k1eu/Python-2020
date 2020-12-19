"""
Zadanie C:
Dana jest pozycja skoczka szachowego, np B7, albo G4. Wyznaczyć wszystkie pola atakowane przez tego skoczka
w jednym ruchu. (Kolumnę pozycji oznaczamy literką A..H, a rząd cyfrą 1..8)
"""
def test(pozycja):
    print(pozycja)
    kolumna = pozycja[0]
    rzad = pozycja[1]
    kolumny = ['A','B','C','D','E','F','G','H']
    rzedy = ['1','2','3','4','5','6','7','8']
    kombinacje = []
    for i in kolumny:
        for j in rzedy:
            kombinacje.append(f'{i}{j}')
    print(kombinacje)
    index_kolumn = kolumny.index(kolumna)
    inedx_rzad = rzedy.index(rzad)

    moves = [f'{kolumny[index_kolumn+2]}{rzedy[inedx_rzad+1]}',
             f'{kolumny[index_kolumn+2]}{rzedy[inedx_rzad-1]}',
             f'{kolumny[index_kolumn-2]}{rzedy[inedx_rzad+1]}',
             f'{kolumny[index_kolumn-2]}{rzedy[inedx_rzad-1]}',
             f'{kolumny[index_kolumn+1]}{rzedy[inedx_rzad+2]}',
             f'{kolumny[index_kolumn-1]}{rzedy[inedx_rzad+2]}',
             f'{kolumny[index_kolumn+1]}{rzedy[inedx_rzad-2]}',
             f'{kolumny[index_kolumn-1]}{rzedy[inedx_rzad-2]}'
             ]
    output = [x for x in moves if kombinacje.__contains__(x)]
    print(output)
    return output
print(test('C2'))