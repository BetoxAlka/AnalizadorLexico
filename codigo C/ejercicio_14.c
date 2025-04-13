
#include <stdio.h>

int main() {
    int vec[]= {1,2,-2,1,3,-1,5,10,-5,2,3}, i, var;
    var = i = 0;
    while(vec[i] < 10) {
        var = var + vec[i];
        ++i;
    }
    printf("%d\n", var);
    return 0;
}
