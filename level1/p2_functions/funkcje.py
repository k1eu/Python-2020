#1 sum of kwadrat elementow listy
w = [1, 2, 3, 4]
x = [1, 2, 3, 2]

def sumofsquare(tab):
    output = 0
    for every in w:
        output += every**2
    return output
print(sumofsquare(w))

#2 highest in lista

print(max(w))

#3 check if rosnaca

def checkIfRosnaca(tab):
    temp = []
    odp = False
    for i in range(len(tab)):
        if i == 0:
            temp.append(tab[i])
        elif i+1 == len(tab):
            if tab[i] > tab[i-1]:
                temp.append(tab[i])
                print('rosnace')
                odp = True
            else:
                print('unlucky')
                break

        else:
            if tab[i] > tab[i-1]:
                temp.append(tab[i])
            else:
                print('unlucky')
                break
    print(temp)
    return odp

print('\nPierwsze')
print(checkIfRosnaca(w))
print('\nDrugie')
print(checkIfRosnaca(x))

#4 czy jest unikalne

def checkIfUnikalne(tab):
    temp = []
    odp = False
    for i in range(len(tab)):
        if i == 0:
            temp.append(tab[i])
        elif i+1 == len(tab):
            if not temp.__contains__(tab[i]):
                temp.append(tab[i])
                odp = True
        else:
            if not temp.__contains__(tab[i]):
                temp.append(tab[i])
            else:
                break
    print(temp)
    return odp

print('\nTrzecie')
print(checkIfUnikalne(w))