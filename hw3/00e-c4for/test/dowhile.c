#include <stdio.h>
// sum(n) = 1+2+...+n
int sum(int n) {
    int s,i;
    s=0;
    i=1;
    do{
        s = s + i;
        i=i+1;
    }while(i <= n);
    return s;
}

int main() {
    printf("sum(10)=%d\n", sum(10));
    return 0;
}
