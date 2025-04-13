
#include <stdio.h>

int main() {
    char c;
    int a = 0, e = 0, i = 0, o = 0, u = 0, count = 0;
    printf("Ingrese 20 caracteres:\n");
    while (count < 20) {
        c = getchar();
        switch(c) {
            case 'a': a++; break;
            case 'e': e++; break;
            case 'i': i++; break;
            case 'o': o++; break;
            case 'u': u++; break;
        }
        count++;
    }
    printf("a=%d e=%d i=%d o=%d u=%d\n", a, e, i, o, u);
    return 0;
}
