import requests

r = requests.get('https://api.github.com/events')
w = r.json()  # to jest tablica słowników/dict

c = sorted(w, key=lambda a:a['actor']['login'])

for i in c:
    print(i['actor'])



w = [['kowalski',2],['nowak',0],['nowak',1], ['zzak',30]]
s1 = sorted(w)
print(s1)

def punkty(lista):
    return lista[1]

s2 = sorted(w, key=punkty)
print(s2)

s3 = sorted(w, key=lambda a: a[1], reverse=True)
print(s3)
