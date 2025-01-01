#include <bits/stdc++.h>

using namespace std;

bool areInSameGroup(const unordered_map<string, int>& groupMap, const string& student1, const string& student2) {
    return groupMap.at(student1) == groupMap.at(student2);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int X, Y, G;
    cin >> X;
    cin.ignore();

    vector<pair<string, string>> mustBeTogether(X);
    for (int i = 0; i < X; ++i) {
        string student1, student2;
        cin >> student1 >> student2;
        mustBeTogether[i] = {student1, student2};
    }

    cin >> Y;
    cin.ignore();

    vector<pair<string, string>> mustBeSeparate(Y);
    for (int i = 0; i < Y; ++i) {
        string student1, student2;
        cin >> student1 >> student2;
        mustBeSeparate[i] = {student1, student2};
    }

    cin >> G;
    cin.ignore();

    unordered_map<string, int> groupMap;
    for (int i = 0; i < G; ++i) {
        string groupLine;
        getline(cin, groupLine);
        stringstream ss(groupLine);
        string student;
        while (ss >> student) {
            groupMap[student] = i;
        }
    }

    int violations = 0;

    for (const auto& constraint : mustBeTogether) {
        if (!areInSameGroup(groupMap, constraint.first, constraint.second)) {
            ++violations;
        }
    }

    for (const auto& constraint : mustBeSeparate) {
        if (areInSameGroup(groupMap, constraint.first, constraint.second)) {
            ++violations;
        }
    }

    cout << violations << endl;
}