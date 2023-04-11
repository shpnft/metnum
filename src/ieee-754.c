#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
        double numero;
        char sinal;
        int expoente;
        char expoente_bin[9];
        char mantissa[25];
        double m;
        int s[25], e, j;

        numero = atof(argv[1]);

        if (numero > 0)
                sinal = '0';
        else
                sinal = '1';

        numero = fabs(numero);
        expoente = floor(log(numero) / log(2));

        m = numero - pow(2, expoente);

        j = 0;
        s[0] = -1;
        for (int i = 0; i < 24; i++) {
                if (m > 0 && s[j] < 0) {
                        e = floor(log(m) / log(2));
                        s[j] = expoente - e - 1;
                        m = m - pow(2, e);
                }
                if (i == s[j]) {
                        mantissa[i] = '1';
                        s[++j] = -1;
                } else
                        mantissa[i] = '0';
        }
        mantissa[24] = '\0';

        expoente = expoente + 127;
        for (int i = 7; i >= 0; i--) {
                expoente_bin[i] = expoente % 2 + '0';
                expoente = expoente / 2;
        }
        expoente_bin[8] = '\0';

        printf("%c%s%s\n", sinal, expoente_bin, mantissa);
        return 0;
}
