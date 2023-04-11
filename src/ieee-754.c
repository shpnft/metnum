#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main(int argc, char **argv) {
        double numero;
        double m,s;
        int expoente,e,c, mantissa;
        numero = atof(argv[1]);

        expoente=floor(log(numero)/log(2));

        m=numero - pow(2,expoente);
        e=expoente;
        if (m > 0) e = floor(log(m)/log(2));
        s=0;
        for (int i=0; i < 23; i++) {
                if (i == expoente-e-1) {
                        s+=pow(2,22-expoente+e+1);
                        m = m - pow(2,e);
                        if (m > 0) e = floor(log(m)/log(2));
                }
        }
        c=0;
        if (expoente-e-1 == 23) c=1;
        mantissa=(int) s+c;
        printf("%d %d\n", expoente+127, mantissa);
        return 0;
}





