x = {}

try:
    print(x['a'])
except:
    print('not working')

x['a'] = 5
try:
    print(x['a'])
except:
    print('znow sie nie udalo')