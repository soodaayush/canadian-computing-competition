#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    int output = 0;

    for (int i = 0; i < n; i++) {
        int total = i * 5;
        int remainder = n - total;

        if (remainder >= 0 and remainder % 4 == 0 ) {
            output++;
        }

        if (remainder < 0) {
            break;
        }
    }

    cout << output << endl;

    return 0;
}
