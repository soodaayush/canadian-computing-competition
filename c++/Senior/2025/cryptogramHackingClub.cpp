#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string S;
    long long c;
    cin >> S >> c;

    vector<pair<char, long long>> pattern;
    long long patternLength = 0;

    for (size_t i = 0; i < S.size();) {
        char character = S[i++];
        long long num = 0;

        while (i < S.size() && isdigit(S[i])) {
            num = num * 10 + (S[i] - '0');
            i++;
        }

        pattern.push_back({character, num});
        patternLength += num;
    }

    c %= patternLength;

    long long position = 0;

    for (auto &[ch, num] : pattern) {
        if (c < position + num) {
            cout << ch << endl;
            break;
        }

        position += num;
    }

    return 0;
}
