#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    int total = 0;

    cin >> n;

    vector<int> h(n + 1), w(n);

    for (int i = 0; i <= n; i++) cin >> h[i];
    for (int i = 0; i < n; i++) cin >> w[i];
    for (int i = 0; i < n; i++) total += (h[i] + h[i + 1]) * w[i];

    if (total / 2 * 2 != total) cout << total / 2 << ".5" << endl;
    else cout << total / 2 << endl;
}