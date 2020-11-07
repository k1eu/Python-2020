def add(a,b):
    return a+b

def diff(a,b):
    return a-b

def calculate(a,b,ff):
    return ff(a,b)

print(calculate(5,7,add))
print(calculate(5, 7, lambda a, b : a if a > b else b))