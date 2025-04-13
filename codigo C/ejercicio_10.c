
#include <stdio.h>

int main() {
    char c;
    int caracteres = 0, palabras = 0, lineas = 0;
    int en_palabra = 0;

    printf("Ingrese un texto (Ctrl+Z para finalizar en Windows, Ctrl+D en Unix):\n");

    while ((c = getchar()) != EOF) {
        caracteres++;
        if (c == '\n') lineas++;
        if (c == ' ' || c == '\t' || c == '\n') {
            if (en_palabra) {
                palabras++;
                en_palabra = 0;
            }
        } else {
            en_palabra = 1;
        }
    }

    if (en_palabra) palabras++;

    printf("Caracteres: %d\nPalabras: %d\nLíneas: %d\n", caracteres, palabras, lineas);
    return 0;
}
