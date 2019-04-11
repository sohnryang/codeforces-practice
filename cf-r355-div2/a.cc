/*
 * Codeforces Round #355 (Div. 2) Problem A
 * https://codeforces.com/contest/677/problem/A
 */

#include <bits/stdc++.h>

using namespace std;

int N, H;

int main() {
    scanf("%d %d", &N, &H);
    int result = 0;
    for (int i = 0; i < N; ++i) {
        int A_i;
        scanf("%d", &A_i);
        result += (int)(A_i > H) + 1;
    }
    printf("%d\n", result);
    return 0;
}
