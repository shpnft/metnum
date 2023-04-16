from math import *
from random import random

def f(x):
    return exp(-x) - x

xa=0
xb=1
print("\\begin{tabular}{c|c|c|c|c|c}")
print("\\(x_a\\) & \\(x_b\\) & \\(x_r\\) & \\(f(x_a)\\) & \\(f(x_b)\\) & \\(f(x_r)\\) \\\\ \hline")
for i in range(20):
    l=[]
    for j in range(6):
        if random() > 0.3:
            l.append("\\bob{{{:.6f}}}")
        else:
            l.append("\\bib{{{:.6f}}}")
    l=" & ".join(l) + " \\\\ \\hline"
    xr=(xa+xb)/2
    fa=f(xa)
    fb=f(xb)
    fr=f(xr)

    print(l.format(xa,xb,xr,fa,fb,fr))
    if fa*fr >= 0:
        xa=xr
    else:
        xb=xr
print("\\end{tabular}")

