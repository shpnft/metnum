from math import log, floor
import sys
try:
    entrada=sys.argv[1]
except IndexError:
    print("Informe um número")
    sys.exit(1)

m=float(entrada)
expoente=floor(log(m)/log(2))

m=m-2**expoente
e=floor(log(m)/log(2))

s=[0]*24
for i in range(24):
    if i == expoente-e-1:
        s[i]=1
        m=m-2**e
        if m == 0: break
        e=floor(log(m)/log(2))

c=s[23]
s="".join(map(str,s[0:23]))
s=int(s,2)+c
print(expoente+127,s)
print(f"0 {expoente+127:0b} {s:0b}")

