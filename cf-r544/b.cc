#include <bits/stdc++.h>

using namespace std;

int N, K;
long long mod_table[101];

int main() {
    scanf("%d %d", &N, &K);
    memset(mod_table, 0, sizeof mod_table);
    for (int i = 0; i < N; ++i) {
        int D_i;
        scanf("%d", &D_i);
        mod_table[D_i % K]++;
    }
    long long result = mod_table[0] / 2;
    mod_table[0] -= ((mod_table[0] / 2) * 2);
    for (int i = 1, j = K - 1; i <= j; ++i, --j) {
        if (i == j) result += (mod_table[i] / 2);
        else result += min(mod_table[i], mod_table[j]);
    }
    printf("%d\n", result * 2);
    return 0;
}
