#include <iostream>
#include <vector>

using namespace std;

int main() {
    int columns = 7;
//    int columns;
//    cin >> columns;

    vector<int> row1 {0, 0, 1, 1, 0, 1, 0};
    vector<int> row2 {0, 0, 1, 0, 1, 0, 0};

//    for (int i = 0; i < columns; i++) cin >> row1[i];
//    for (int i = 0; i < columns; i++) cin >> row2[i];

    int perimeter = 0;

    for (int i = 0; i < columns; i++) {
        if (row1[i] == 1) {
            perimeter += 3;

            if (i > 0 && row1[i - 1] == 1) {
                perimeter--;
            }

            if (row2[i] == 1) {
                perimeter--;
            }
        }

        if (row2[i] == 1) {
            perimeter += 3;

            if (i > 0 && row2[i - 1] == 1) {
                perimeter--;
            }

            if (row1[i] == 1) {
                perimeter--;
            }
        }
    }

    cout << perimeter << endl;
}
