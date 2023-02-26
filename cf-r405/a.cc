#include <bits/stdc++.h>

using namespace std;

int main() {
    int A, B;
    scanf("%d %d", &A, &B);
    int result = 0;
    while (A <= B) {
        A *= 3;
        B *= 2;
        result++;
    }
    printf("%d\n", result);
    return 0;
}
