#include <bits/stdc++.h>

using namespace std;

int main() {
    int columns;
    int perimeter = 0;
    cin >> columns;

    vector<int> row1(columns);
    vector<int> row2(columns);

    for (int i = 0; i < columns; i++) cin >> row1[i];
    for (int i = 0; i < columns; i++) cin >> row2[i];

    for (int i = 0; i < columns; i++) {
        if (row1[i]) perimeter += 3;
        if (row2[i]) perimeter += 3;

        if (i % 2 == 0) {
            if (row1[i] && row2[i]) {
                perimeter -= 2;
            }
        }

        if (i > 0) {
            if (row1[i] && row1[i - 1]) perimeter -= 1;
            if (row2[i] && row2[i - 1]) perimeter -= 1;
        }

        if (i < columns - 1) {
            if (row1[i] && row1[i + 1]) perimeter -= 1;
            if (row2[i] && row2[i + 1]) perimeter -= 1;
        }
    }

    cout << perimeter << endl;
}
