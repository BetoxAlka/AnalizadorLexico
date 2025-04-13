
#include <stdio.h>

int main() {
    char letras[26];
    for (int i = 0; i < 26; i++) {
        letras[i] = 'a' + i;
    }

    printf("Letras del alfabeto:\n");
    for (int i = 0; i < 26; i++) {
        printf("%c ", letras[i]);
    }
    printf("\n");

    return 0;
}
