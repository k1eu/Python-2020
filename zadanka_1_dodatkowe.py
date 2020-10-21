from datetime import datetime
from time import sleep


# test setów
timestamp1 = datetime.now().timestamp()
w = [1, 2, 3, 2]
g = [1, 5, 7, 2]

a = set()
b = set()

for i in w:
    a.add(i)
for i in g:
    b.add(i)
p = a.intersection(b)
print(p)

# zad.4 przerobione na sety
def checkIfUnikalne(tab):
    temp = set()
    odp = False
    for i in range(len(tab)):
        if i == 0:
            temp.add(tab[i])
        else:
            if temp.__contains__(tab[i]):
                odp = False
                break
            else:
                temp.add(tab[i])
                odp = True
    print(temp)
    return odp

print(checkIfUnikalne(w))

# test pomiaru czasu
sleep(0.5)
timestamp2 = datetime.now().timestamp()
print(f'Minelo: {timestamp2-timestamp1:.2f}') # ile minelo ucięte do 2ch po przecinku


