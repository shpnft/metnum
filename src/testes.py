from random import randrange, random

def sciExpoent():
    n = 0
    while n in [-1,0,1]:
        n = randrange(-30,30)
    return str(n)

def intStream(n):
    return "".join(map(str,[randrange(10) for i in range(n)]))

r = random()

if r < 0.25:
    n = randrange(9)
    m = intStream(n)
    s = "0"*(9-n)
    print(f"0.{s}{m}")
elif r < 0.5:
    n = randrange(300)
    m = intStream(9)
    print(f"{n}.{m}")
else:
    n = randrange(300)
    m = intStream(9)
    e = sciExpoent()
    print(f"{n}.{m}e{e}")
