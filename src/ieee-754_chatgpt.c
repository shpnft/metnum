#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

typedef union {
    float f;
    uint32_t i;
} Float;

void print_binary(uint32_t num, int bits) {
    for (int i = bits - 1; i >= 0; i--) {
        printf("%d", (num >> i) & 1);
    }
}

int main(int argc, char **argv) {
    float num;
    num = atof(argv[1]);
    
    Float f;
    f.f = num;
    
    printf("\'\'%s,\'",argv[1]);
    print_binary(f.i, 32);
    printf("\n");
    
    return 0;
}

