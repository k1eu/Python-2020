from random import randint
from datetime import datetime

# GENEROWANIE 10**5 liczb losowych z przedzialu 1..10**4
# DLA 10**5 liczb:
# Generowanie 0.14
# Dodawanie liczb 0.09
# Razem z petla  0.4
# Szukanie unikalnych 4.89

# Dla 10**6 liczb:
# Generowanie 1.59
# Dodawanie 0.8
# Razem z petla 4.20
# Szukanie unikalnych 51.23

# Brak jeszcze danych z VM'a

random_numbers = []
time_generating = 0.00
time_adding = 0.00

timestamp1 = datetime.now().timestamp()
for i in range(10**5):
    timestamp2 = datetime.now().timestamp()
    temp = randint(1, 10**4)
    timestamp3 = datetime.now().timestamp()
    time_generating += (timestamp3-timestamp2)

    timestamp4 = datetime.now().timestamp()
    random_numbers.append(temp)
    timestamp5 = datetime.now().timestamp()
    time_adding += (timestamp5-timestamp4)
timestamp6 = datetime.now().timestamp()
time_alltogether = timestamp6-timestamp1

print(f'Time spent alltogether = {time_alltogether}\n'
      f'Time spent generating numbers = {time_generating}\n'
      f'Time spent adding numbers to lists = {time_adding}')

# WYLICZENIE ELEMENTOW UNIKALNYCH

unikalne = 0
sprawdzone = 0
unikalna_lista = []
timestamp7 = datetime.now().timestamp()
for i in range(len(random_numbers)):
    if i == 0:
        unikalna_lista.append(random_numbers[i])
        unikalne += 1
    else:
        if unikalna_lista.__contains__(random_numbers[i]):
            sprawdzone += 1
        else:
            unikalna_lista.append(random_numbers[i])
            sprawdzone += 1
            unikalne += 1
timestamp8 = datetime.now().timestamp()
print(f'\nTyle jest liczb unikalnych: {unikalne} / {sprawdzone}\n'
      f'Sprawdzanie unikalności zajęło tyle czasu: {(timestamp8-timestamp7):.2f}')


# GENEROWANIE 10**6 LICZB LOSOWYCH Z PRZEDZIALU 1..10**4

random_numbers2 = []
time_generating2 = 0.00
time_adding2 = 0.00

timestamp12 = datetime.now().timestamp()
for i in range(10**6):
    timestamp22 = datetime.now().timestamp()
    temp = randint(1, 10**4)
    timestamp32 = datetime.now().timestamp()
    time_generating2 += (timestamp32-timestamp22)

    timestamp42 = datetime.now().timestamp()
    random_numbers2.append(temp)
    timestamp52 = datetime.now().timestamp()
    time_adding2 += (timestamp52-timestamp42)
timestamp62 = datetime.now().timestamp()
time_alltogether2 = timestamp62-timestamp12

print(f'\nTime spent alltogether = {time_alltogether2}\n'
      f'Time spent generating numbers = {time_generating2}\n'
      f'Time spent adding numbers to lists = {time_adding2}')

# LICZENIE UNIKALNOSCI DLA 10**6 LICZB LOSOWYCH

unikalne2 = 0
sprawdzone2 = 0
unikalna_lista2 = []
timestamp72 = datetime.now().timestamp()
for i in range(len(random_numbers2)):
    if i == 0:
        unikalna_lista2.append(random_numbers2[i])
        unikalne2 += 1
    else:
        if unikalna_lista2.__contains__(random_numbers2[i]):
            sprawdzone2 += 1
        else:
            unikalna_lista2.append(random_numbers2[i])
            sprawdzone2 += 1
            unikalne2 += 1
timestamp82 = datetime.now().timestamp()
print(f'\nTyle jest liczb unikalnych: {unikalne2} / {sprawdzone2}\n'
      f'Sprawdzanie unikalności zajęło tyle czasu: {(timestamp82-timestamp72):.2f}')