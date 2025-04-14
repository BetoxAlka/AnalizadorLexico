
#include <stdio.h>
#include <ctype.h>

int main() {
    char cadena[100];
    int no_digitos = 0, blancos = 0;
    printf("Ingrese una cadena: ");
    fgets(cadena, 100, stdin);

    for (int i = 0; cadena[i] != '\0'; i++) {
        if (!isdigit(cadena[i]) && cadena[i] != '\n')
            no_digitos++;
        if (cadena[i] == ' ')
            blancos++;
    }

    printf("La cantidad de no dígitos es: %d\n", no_digitos);
    printf("La cantidad de blancos es: %d\n", blancos);

    return 0;
}
