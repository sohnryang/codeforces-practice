#include <bits/stdc++.h>

using namespace std;

int N, A[1001];

int area_size(int i) {
    int result = 1;
    for (int l = i - 1; l >= 0; --l) {
        if (A[l] > A[l + 1]) break;
        result++;
    }
    for (int r = i + 1; r < N; ++r) {
        if (A[r] > A[r - 1]) break;
        result++;
    }
    return result;
}

int main() {
    scanf("%d", &N);
    for (int i = 0; i < N; ++i)
        scanf("%d", &A[i]);
    int result = 0;
    for (int i = 0; i < N; ++i)
        result = max(result, area_size(i));
    printf("%d\n", result);
    return 0;
}
