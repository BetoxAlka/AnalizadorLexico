
#include <stdio.h>

int main() {
    int num, mayor, menor;
    printf("Ingrese 5 números:\n");
    scanf("%d", &num);
    mayor = menor = num;

    for (int i = 1; i < 5; i++) {
        scanf("%d", &num);
        if (num > mayor) mayor = num;
        if (num < menor) menor = num;
    }

    printf("Mayor: %d\nMenor: %d\n", mayor, menor);
    return 0;
}
