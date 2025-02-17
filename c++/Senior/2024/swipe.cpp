#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> a(n);
    vector<int> b(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    for (int i = 0; i < n; i++) {
        cin >> b[i];
    }

    vector<vector<int>> important;

    int target = b[0];
    int aIndex = 0;

    for (int i = 0; i < n; i++) {
        while (i < n && b[i] == target) {
            i++;
        }

        while (aIndex < n && a[aIndex] != target) {
            aIndex++;
        }

        if (aIndex >= n) {
            cout << "NO" << endl;
            return 0;
        }

        important.push_back({target, aIndex});
        target = b[i];
        i--;
    }

    cout << "YES" << endl;

    vector<vector<int>> leftMoves;

    int left = 0;
    target = b[0];
    int impIndex = 0;

    for (int i = 0; i < n && impIndex < important.size(); i++, impIndex++) {
        while (i < n && b[i] == target) {
            i++;
        }

        if (important[impIndex][1] > left) {
            leftMoves.push_back({left, important[impIndex][1]});
        }

        target = b[i];
        left = i;
    }

    vector<vector<int>> rightMoves;

    int right = n - 1;
    target = b[n - 1];
    impIndex = important.size() - 1;

    for (int i = n - 1; i >= 0 && impIndex >= 0; i--, impIndex--) {
        while (i >= 0 && b[i] == target) {
            i--;
        }

        if (important[impIndex][1] < right){
            rightMoves.push_back({important[impIndex][1], right});
        }

        target = b[i];
        right = i;
    }

    cout << leftMoves.size() + rightMoves.size() << endl;
    for (auto& m: leftMoves){
        cout << "L " << m[0] << ' ' << m[1] << endl;
    }
    for (auto& m: rightMoves){
        cout << "R " << m[0] << ' ' << m[1] << endl;
    }
}