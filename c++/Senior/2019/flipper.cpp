#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<vector<int>> grid = {{1, 2}, {3, 4}};

    string flips;
    cin >> flips;

    for (int i = 0; i < flips.length(); i++) {
        int num1 = grid[0][0];
        int num2 = grid[1][0];
        int num3 = grid[0][1];
        int num4 = grid[1][1];

        if (flips[i] == 'H') {
            grid[0][0] = num2;
            grid[0][1] = num4;
            grid[1][0] = num1;
            grid[1][1] = num3;
        } else {
            grid[0][0] = num3;
            grid[0][1] = num1;
            grid[1][0] = num4;
            grid[1][1] = num2;
        }
    }

    cout << grid[0][0] << " " << grid[0][1] << endl;
    cout << grid[1][0] << " " << grid[1][1] << endl;
}