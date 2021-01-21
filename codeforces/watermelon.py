w = int(input())


def watermelon_even_split(p = w):
    l: int
    r: int
    if p >= 1 and p <= 100 and p % 2 == 0:
        temp = p/2
        if temp.is_integer():
            temp = int(temp)
        l = temp
        r = temp
        if temp % 2 == 0:
            return 'YES'
        for i in range(1,temp):
            l -= 1
            r += 1
            if l % 2 == 0 and r % 2 == 0:
                return 'YES'
        return 'NO'
    return 'NO'

print(watermelon_even_split(w))