# https://codeforces.com/problemset/problem/282/A

n = int(input())
result = 0
for i in range(0,n):
    temp = input()
    if temp.__contains__('++'):
        result+=1
    elif temp.__contains__('--'):
        result-=1
print(result)

