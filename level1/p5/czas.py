from datetime import datetime


def ts():
    return datetime.now().timestamp()


st = ts()

for i in range(1000):
    b = datetime.now()
    print(f'data:{b}, rok:{b.year}, czas UTC: {datetime.utcfromtimestamp(b.timestamp())}, timestamp:{b.timestamp()}')

end = ts()
print(f'wydrukowanie 100 liczb trwało: {(end - st) * 1000:.3f}ms')