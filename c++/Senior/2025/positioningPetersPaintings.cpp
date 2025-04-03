#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long A, B, X, Y;
    cin >> A >> B >> X >> Y;

    long long option1 = 2 * (A + X + max(B, Y));
    long long option2 = 2 * (max(A, X) + B + Y);

    cout << min(option1, option2) << endl;
}

