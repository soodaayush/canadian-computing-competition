#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int main() {
    int wordCount, letterCount;
    cin >> wordCount >> letterCount;

    unordered_map<char, int> map;

    for (int i = 0; i < wordCount; i++) {
        string word;
        cin >> word;

        for (char c: word) {
            map[c]++;
        }

        for (int j = 0; j < letterCount; j++) {
            if ((map[word[j]] > 1 && map[word[j + 1]] > 1) || (map[word[j]] == 1 && map[word[j + 1]] == 1)) {
                cout << "F" << endl;
                break;
            } else if (j == letterCount - 1) {
                cout << "T" << endl;
            }
        }

        map.clear();
    }


    return 0;
}
