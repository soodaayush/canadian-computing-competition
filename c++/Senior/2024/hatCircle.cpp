#include <bits/stdc++.h>

using namespace std;

int main() {
    int peopleCount;
    cin >> peopleCount;

    vector<int> array(peopleCount);

    for (int i = 0; i < peopleCount; i++) {
        cin >> array[i];
    }

    int counter = 0;

    for (int i = 0; i < peopleCount; i++) {
        if (array[i] == array[(i + peopleCount / 2) % peopleCount]) {
            counter++;
        }
    }

    cout << counter << endl;
}
