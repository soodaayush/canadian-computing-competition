#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int sameGroupCount, differentGroupCount, groupCount;
    int violations = 0;

    vector<string> sameGroup;
    vector<string> differentGroup;
    vector<string> group;

    cin >> sameGroupCount;
    if (sameGroupCount > 0) for (int i = 0; i < sameGroupCount; i++) cin >> sameGroup[i];

    cin >> differentGroupCount;
    if (differentGroupCount > 0)  for (int i = 0; i < differentGroupCount; i++) cin >> differentGroup[i];

    cin >> groupCount;
    if (groupCount > 0)  for (int i = 0; i < groupCount; i++) cin >> group[i];

    int count = 0;

    if (sameGroupCount > 0) {
        for (const auto& elem : sameGroup) {
            // Check each inner vector in vec2
            for (const auto& innerVec : group) {
                // If element from vec1 is found in the inner vector, increment the count
                if (find(innerVec.begin(), innerVec.end(), elem) != innerVec.end()) {
                    ++count;
                    break;  // Stop checking further inner vectors once a match is found
                }
            }
        }
    }
}