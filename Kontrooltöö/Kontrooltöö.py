from math import *
from random import *

print("VARIANT N.2")
print()
print("Ülesanne N.1")
print()
try:
    n = int(input("vali number 1 kuni 9: "))
    while n:
        if n < 1 or n > 9:
            print("error")
            break
        else:
            for i in range(3):
                for j in range(n):
                    if i == 0:
                        print(" (\_/)   ", end="")
                    elif i == 1:
                        print(" (o o)   ", end="")
                    elif i == 2:
                        print(" / | \*  ", end="")
                print("")
            break
except:
    print("Vale andmetüüp")

print()
print("Ülesanne N.2")
print()

try:
    L = int(input("Vali number: "))
    s = 0
    for i in range(L+1):
        s += i
    print("Tarvude summa 0 kuni", L, "on", s)
except:
    print("Vali andmetüüp")

print()
print("Ülesanne N.3")
print()

n = randint(0, 100)
k = 0
while k < 10:
    try:
        g = int(input("Arvake arv vahemikus 0 kuni 100: "))
        if g < 0 or g > 100:
            print("Arvake arv vahemikus 0 kuni 100")
            continue
    except:
        print("Vale andmetüüp")
        break
    if g == n:
        print("Palju õnne! Sa arvasid numbri ära", k + 1, "katsed!")
        break
    elif g < n:
        print("Arv on suurem kui teie oletus.")
    else:
        print("Arv on väiksem, kui arvate.")
    k += 1
if k == 10:
    print("Vabandust, sa ei arvanud numbrit 10 katsega ära. Number oli", n)


print()
print("Ülesanne N.4")
print()
try:
    n = int(input("Vali number: "))
    r = 0
    while n > 0:
        x = n % 10
        r = r * 10 + x
        n = n // 10
    print("ümberpööratud arv:", r)
except:
    print("Vale andmetüüp")

print()
print("Ülesanne N.5")
print()
try:
    n = int(input("Vali number: "))
    s = 0
    p = 1
    while n > 0:
        d = n % 10
        s += d
        p *= d
        n = n // 10
    print("Numbrite summa on:", s)
    print("Numbrite korrutis on:", p)
except:
    print("Vale admetüüp")