#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int m, n, k;
    int count = 0;

    cin >> m;
    cin >> n;
    cin >> k;

    vector<vector<int>> grid(m, vector<int>(n, 0));


    for (int i = 0; i < k; i++) {
        char letter;
        int location;
        cin >> letter >> location;

        if (letter == 'R') {
            int r = 0;

            for (int j = 0; j < n; j++) {
                if (grid[location - 1][r] == 0) {
                    grid[location - 1][r] = 1;
                } else {
                    grid[location - 1][r] = 0;
                }

                r++;
            }
        } else {
            int r = 0;

            for (int j = 0; j < m; j++) {
                if (grid[r][location - 1] == 0) {
                    grid[r][location - 1] = 1;
                } else {
                    grid[r][location - 1] = 0;
                }

                r++;
            }
        }
    }

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) {
                count++;
            }
        }
    }

    cout << count << endl;
}