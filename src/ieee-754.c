#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    double numero;
    char sinal;
    int expoente;
    char expoenteBin[9];
    char mantissa[25];
    double m;
    int s, e;

    numero = atof(argv[1]);

    if (numero > 0)
        sinal = '0';
    else
        sinal = '1';

    numero = fabs(numero);
    expoente = floor(log(numero) / log(2));

    m = numero - pow(2, expoente);
    s = -1;
    for (int i = 0; i < 24; i++) {
        if (m > 0 && s < 0) {
            e = floor(log(m) / log(2));
            s = expoente - e - 1;
            m = m - pow(2, e);
        }
        if (i == s) {
            mantissa[i] = '1';
            s = -1;
        } else
            mantissa[i] = '0';
    }

    if (mantissa[23] == '1') {
        s = 22;
        while (mantissa[s] == '1' && s >= 0)
            s = s - 1;
        if (s < 0)
            expoente = expoente + 1;
        else
            mantissa[s] = '1';

        for (s = s + 1; s < 23; s++)
            mantissa[s] = '0';
    }
    mantissa[23] = '\0';

    expoente = expoente + 127;
    for (int i = 7; i >= 0; i--) {
        expoenteBin[i] = expoente % 2 + '0';
        expoente = expoente / 2;
    }
    expoenteBin[8] = '\0';

    printf("%c%s%s\n", sinal, expoenteBin, mantissa);
    return 0;
}
