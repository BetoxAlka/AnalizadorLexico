
#include <stdio.h>

int main() {
    int num;
    do {
        printf("Ingrese un numero entre 1 y 5: ");
        num = getchar() - '0';
        while(getchar() != '\n'); // Limpiar buffer
    } while (num < 1 || num > 5);
    printf("Numero valido: %d\n", num);
    return 0;
}
