from random import random

def printBi(f,xa,xb):
    print("\\begin{tabular}{c|c|c|c|c|c|l}")
    print(f"iteração & \(x_a\) & \(x_b\) & \(x_r\) & \(f(x_a)\) & \(f(x_b)\) & \(f(x_r)\) \\\\ \\hline")

    for i in range(20):
        xr=(xa+xb)/2
        fa=f(xa)
        fb=f(xb)
        fr=f(xr)
        template = "{}  "
        for j in range(6):
            r=random()
            if r < 0.4:
                template = template + "& \\bob{{{:.6f}}}"
            else:
                template = template + "& \\bib{{{:.6f}}}"
        template =  template + "\\\\ \\hline"
        print(template.format(i,xa,xb,xr,fa,fb,fr))
        if fa*fr >= 0:
            xa=xr
        else:
            xb=xr
    print("\\end{tabular}")
