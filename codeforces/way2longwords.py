n = int(input())
for i in range(0,n):
    temp = input()
    if len(temp) > 10:
        frst_lttr = temp[0]
        last_lttr = temp[-1]
        number = len(temp) - 2
        print(f'{frst_lttr}{number}{last_lttr}')
    else:
        print(temp)