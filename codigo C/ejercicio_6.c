
#include <stdio.h>

int main() {
    int count = 0;
    for (int i = 100; i >= 20; i--) {
        if (i % 2 == 0) {
            printf("%3d   ", i);
            count++;
            if (count % 6 == 0)
                printf("\n");
        }
    }
    return 0;
}
