#include <bits/stdc++.h>

using namespace std;

int countDistinctPermutations(const string& N, const string& H) {
    int n = N.length(), h = H.length();
    if (n > h) return 0;

    vector<int> nFreq(26, 0), windowFreq(26, 0);
    unordered_set<string> distinctPerms;

    // Count frequency of characters in N
    for (char c : N) nFreq[c - 'a']++;

    // Initialize the first window
    for (int i = 0; i < n; i++) windowFreq[H[i] - 'a']++;

    // Check if the first window is a permutation
    if (nFreq == windowFreq) distinctPerms.insert(H.substr(0, n));

    // Slide the window
    for (int i = n; i < h; i++) {
        windowFreq[H[i - n] - 'a']--;
        windowFreq[H[i] - 'a']++;

        if (nFreq == windowFreq) {
            distinctPerms.insert(H.substr(i - n + 1, n));
        }
    }

    return distinctPerms.size();
}

int main() {
    string N, H;
    cin >> N >> H;
    cout << countDistinctPermutations(N, H) << endl;
    return 0;
}
