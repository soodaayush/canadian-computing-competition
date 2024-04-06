#include <iostream>
using namespace std;

int main() {
    int dusaSize;
    cin >> dusaSize;

    while (true) {
        int yobiSize;
        cin >> yobiSize;

        if (yobiSize < dusaSize) {
            dusaSize += yobiSize;
        }

        if (yobiSize >= dusaSize) {
            break;
        }
    }

    cout << dusaSize << endl;
}