n, k = input().split()
n = int(n)
k = int(k)
temp = input().split()
temp2 = []
last_spot : int
for i in temp:
    temp2.append(int(i))
temp3 = []
for i in range(len(temp2)):
    if temp2[i] == 0:
        break
    if i <= k-1:
        temp3.append(temp2[i])
    if i > k-1:
        if temp2[i] == temp2[k-1]:
            temp3.append(temp2[i])
print(len(temp3))
