#include <bits/stdc++.h>

using namespace std;

int main() {
    int N, A, T[101];
    scanf("%d %d", &N, &A);
    for (int i = 1; i <= N; ++i)
        scanf("%d", &T[i]);
    int result = T[A], left = A - 1, right = A + 1;
    while (left >= 1 || right <= N) {
        if (left <= 0) result += T[right];
        else if (right > N) result += T[left];
        else if (T[left] + T[right] == 2) result += 2;
        left--;
        right++;
    }
    printf("%d\n", result);
    return 0;
}
