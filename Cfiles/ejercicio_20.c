
#include <stdio.h>

int suma(int a, int b) {
    return a + b;
}

void resta(int a, int b) {
    printf("Resultado de la resta: %d\n", a - b);
}

float divi(int a, int b) {
    if (b == 0) {
        printf("Error: división por cero.\n");
        return 0;
    }
    return (float)a / b;
}

int main() {
    int a, b, opcion;
    printf("Ingrese dos números enteros: ");
    scanf("%d %d", &a, &b);

    printf("Menú de opciones:\n");
    printf("1- SUMAR\n2- RESTAR\n3- MULTIPLICAR\n4- DIVIDIR\n");
    printf("Seleccione una opción: ");
    scanf("%d", &opcion);

    switch(opcion) {
        case 1:
            printf("Resultado de la suma: %d\n", suma(a, b));
            break;
        case 2:
            resta(a, b);
            break;
        case 3:
            printf("Resultado de la multiplicación: %d\n", a * b);
            break;
        case 4:
            printf("Resultado de la división: %.2f\n", divi(a, b));
            break;
        default:
            printf("Opción no válida.\n");
    }

    return 0;
}
