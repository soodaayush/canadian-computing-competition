#include <bits/stdc++.h>

using namespace std;

struct path {
    int dest;
    int ind;
};

vector<char> ans;

void solve(int cur, vector<vector<path>>& graph, vector<bool>& visited, bool red) {
    visited[cur] = true;

    for (auto& p : graph[cur]) {
        if (!visited[p.dest]) {
            ans[p.ind] = red ? 'R' : 'B';
            solve(p.dest, graph, visited, !red);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<path>> graph (n + 1);
    vector<bool> vis (n + 1, false);

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back({v, i});
        graph[v].push_back({u, i});
    }

    ans.resize(m, 'G');

    for (int i = 0; i < n; i++) {
        if (!vis[i + 1]) solve(i + 1, graph, vis, true);
    }

    for (auto& c: ans) cout << c;
}