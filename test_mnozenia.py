from random import randint
from datetime import datetime


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

correct = 0
total = 0
total_time = 0 # w sekundach
liczby_a = []
liczby_b = []
odpowiedzi = []
punkty = []
times = []

for i in range(10): #
    a = randint(1,16)
    b = randint(1,16)
    start = datetime.now()
    w = input(f'podaj wynik mnożenia {a} * {b} > ')
    end = datetime.now()
    tymczasowy_czas = end - start
    times.append(tymczasowy_czas)
    obliczone_sekundy = str(tymczasowy_czas.seconds)
    obliczone_ms = f'{tymczasowy_czas.microseconds}'
    obliczony_czas = obliczone_sekundy +'.'+ obliczone_ms
    total_time += float(obliczony_czas) # total_time = total_time + obliczony_czas
    print(total_time)
    #wynik = int(w) # zamiana na liczbe
    wynik = str(a * b)
    if w == wynik:
        print('Zgadza się, +1')
        correct += 1
        punkty.append(1)
    else:
        print('Źle, +0')
        punkty.append(0)

    total += 1
    liczby_a.append(a)
    liczby_b.append(b)
    odpowiedzi.append(w)
    print(f'wynik tymczasowy to: {correct} / {total} = {correct / total * 100 :.2f}%')

for i in range(10): # 0 1 2 3 4 5 6 7 8 9
    print(f'{i+1}. Wylosowano a : {liczby_a[i]} b : {liczby_b[i]} | odpowiedź : {odpowiedzi[i]} | punkty {punkty[i]} | czas odpowiedzi: {times[i].seconds}.{times[i].microseconds} sek')
print(f'Podsumowanie: Punkty : {correct} / {total} = {correct / total * 100 :.2f}% | Czas wykonania łącznie : {total_time:.2f} sek')

plik = open("highscore.txt","a")
plik.write(f'Podsumowanie: Punkty : {correct} / {total} = {correct / total * 100 :.2f}% | Czas wykonania łącznie : {total_time:.2f} sek \n')
plik.close()