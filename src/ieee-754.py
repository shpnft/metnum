from math import floor, log
import sys

numero = float(sys.argv[1])

if numero > 0:
    sinal = "0"
else:
    sinal = "1"

numero = abs(numero)
expoente = floor(log(numero) / log(2))

m = numero - 2**expoente
mantissa = ""
s = -1
for i in range(24):
    if m > 0 and s < 0:
        e = floor(log(m) / log(2))
        s = expoente - e - 1
        m = m - 2**e
    if i == s:
        mantissa = mantissa + "1"
        s = -1
    else:
        mantissa = mantissa + "0"

if mantissa[23] == "1":
    s = 22
    while mantissa[s] == "1" and s >= 0:
        s = s - 1
    if s < 0:
        expoente = expoente + 1
        mantissa = "0"
    else:
        mantissa = mantissa[0:s] + "1"
    for i in range(s + 1, 23):
        mantissa = mantissa + "0"

mantissa = mantissa[0:23]

expoente = expoente + 127
expoenteBin = ""
for i in range(8):
    expoenteBin = ["0", "1"][expoente % 2] + expoenteBin 
    expoente = expoente // 2

print(f"{sinal}{expoenteBin}{mantissa}")
