
#include <stdio.h>

int es_primo(int n) {
    if (n < 2) return 0;
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0) return 0;
    return 1;
}

int main() {
    int n;
    char continuar;
    do {
        printf("Ingrese un número: ");
        scanf("%d", &n);
        printf("Números primos hasta %d:\n", n);
        for (int i = 1; i <= n; i++) {
            if (es_primo(i))
                printf("%d ", i);
        }
        printf("\nDesea continuar? (s/n): ");
        scanf(" %c", &continuar);
    } while (continuar == 's');
    return 0;
}
