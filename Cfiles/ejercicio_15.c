
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int numeros[100], n, suma = 0;
    srand(time(NULL));

    for (int i = 0; i < 100; i++) {
        numeros[i] = rand() % 1000;
    }

    printf("Ingrese un número: ");
    scanf("%d", &n);

    printf("Números mayores o iguales a %d:\n", n);
    for (int i = 0; i < 100; i++) {
        if (numeros[i] >= n) {
            printf("%d ", numeros[i]);
            suma += numeros[i];
        }
    }

    printf("\nLa sumatoria de los números mayores o iguales a %d es %d\n", n, suma);
    return 0;
}
