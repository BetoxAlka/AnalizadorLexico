
#include <stdio.h>

int main() {
    int j = 0, n;
    printf("Ingrese un valor para n: ");
    scanf("%d", &n);

    printf("Con for:\n");
    for (j = 0; j <= n; j++) printf("%d ", j);

    printf("\nCon while:\n");
    j = 0;
    while (j <= n) { printf("%d ", j); j++; }

    printf("\nCon do-while:\n");
    j = 0;
    do { printf("%d ", j); j++; } while (j <= n);

    return 0;
}
