from math import floor,log
import sys

numero = float(sys.argv[1])

if numero > 0: sinal='0'
else: sinal='1'

numero = abs(numero)
expoente = floor(log(numero)/log(2))

m = numero - 2**expoente

s=-1
mantissa=""
for i in range(24):
    if m > 0 and s < 0:
        e = floor(log(m)/log(2))
        s = expoente - e - 1
        m = m - 2**e
    if i == s:
        mantissa = mantissa + '1'
        s = -1
    else:
        mantissa = mantissa + '0'

expoente=expoente+127
expoente_bin=[]
for i in range(8):
    expoente_bin.append(str(expoente%2))
    expoente = expoente // 2
expoente_bin.reverse()
expoente_bin = "".join(expoente_bin)

print(f"{sinal}{expoente_bin}{mantissa}")
