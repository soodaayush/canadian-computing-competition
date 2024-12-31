#include <bits/stdc++.h>

using namespace std;

int main() {
    int n = 0;
    double speed = 0;
    pair<double, double> observation[100005];
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> observation[i].first>>observation[i].second;
    }
    sort(observation, observation + n);
    for (int i = 1; i < n; i++) {
        speed = max(speed, abs(observation[i].second - observation[i - 1].second)/(observation[i].first - observation[i - 1].first));
    }

    cout << speed;
}