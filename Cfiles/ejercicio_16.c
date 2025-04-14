
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void ordenar(int arr[], int tam, int asc) {
    for (int i = 0; i < tam - 1; i++) {
        for (int j = i + 1; j < tam; j++) {
            if ((asc && arr[i] > arr[j]) || (!asc && arr[i] < arr[j])) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

int main() {
    int numeros[100], criterio;
    srand(time(NULL));
    for (int i = 0; i < 100; i++) {
        numeros[i] = rand() % 1000;
    }

    printf("Ingrese 1 para orden ascendente o 0 para descendente: ");
    scanf("%d", &criterio);

    ordenar(numeros, 100, criterio);

    printf("Números ordenados:\n");
    for (int i = 0; i < 100; i++) {
        printf("%d ", numeros[i]);
    }
    printf("\n");
    return 0;
}
