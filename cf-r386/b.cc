#include <bits/stdc++.h>

using namespace std;

int main() {
    int N;
    char S[2001], result[2001];
    memset(result, 0, sizeof result);
    scanf("%d", &N);
    scanf("%s", S);
    int left = 0, right = N - 1;
    for (int i = 0; i < N; ++i) {
        if (i % 2 == 0) {
            result[right] = S[N - i - 1];
            right--;
        } else {
            result[left] = S[N - i - 1];
            left++;
        }
    }
    printf("%s\n", result);
    return 0;
}
