n = int(input())
result = 0
for i in range(0,n):
    x,y,z = input().split()
    tab = [int(x), int(y), int(z)]
    result += 1 if sum(tab) >= 2 else 0
print(result)


