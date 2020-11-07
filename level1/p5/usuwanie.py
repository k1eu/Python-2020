from datetime import datetime


def ts():
    return datetime.now().timestamp()


st = ts()
w = [1]*10**5*4
end = ts()
print(f'tworzenie 10**7 liczb trwało: {(end - st) * 1000:.3f}ms')

st2 = ts()

#for i in range(len(w)):
#    del w[0]
for i in range(len(w)):
    del w[-1]

end2 = ts()
print(w)
print(f'usuwanie 10**7 liczb trwało: {(end2 - st2) * 1000:.3f}ms')

#usuwanie 10**7 liczb trwało: 907.527ms
#usuwanie 10**7 liczb trwało: 7140.144ms vs usuwanie 10**7 liczb trwało: 35.032ms

# usuwanie od przodu kopiuje i rosnie kwadratowo
# usuwanie od tylu jest duzo szybsze i rosnie liniowo
