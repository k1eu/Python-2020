import requests
from time import sleep

unique_logins = {}

def recent_logins():
    # zbiera loginname userów 30 ostatnich zdarzeń na github
    requested_data = requests.get('https://api.github.com/events')
    data_value = requested_data.json()  # to jest tablica słowników/dict
    users = []
    unique_users = {}
    for e in data_value:
        users.append(e['actor']['login'])
        unique_users[e['actor']['login']] = 1
    return unique_users


for i in range(12): # 0 1 2 3 4 5 6 7 8 9 10 11 12
    unique_logins.update(recent_logins())
    print(unique_logins)
    sleep(10)

print(unique_logins.keys())