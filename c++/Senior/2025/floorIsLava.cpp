#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

struct Connection {
    int destination;
    ll cost;
};

struct Tunnel {
    int roomA, roomB;
    ll requiredChill;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int numRooms, numTunnels;
    cin >> numRooms >> numTunnels;

    vector<vector<ll>> possibleChillingLevels(numRooms);
    vector<Tunnel> tunnels;
    tunnels.reserve(numTunnels);

    for (int i = 0; i < numTunnels; i++) {
        int roomA, roomB;
        ll requiredChill;
        cin >> roomA >> roomB >> requiredChill;
        roomA--; roomB--;
        tunnels.push_back({roomA, roomB, requiredChill});
        possibleChillingLevels[roomA].push_back(requiredChill);
        possibleChillingLevels[roomB].push_back(requiredChill);
    }

    possibleChillingLevels[0].push_back(0);

    for (int i = 0; i < numRooms; i++) {
        sort(possibleChillingLevels[i].begin(), possibleChillingLevels[i].end());
        possibleChillingLevels[i].erase(unique(possibleChillingLevels[i].begin(), possibleChillingLevels[i].end()), possibleChillingLevels[i].end());
    }

    vector<int> roomStartIndex(numRooms, 0);
    int totalStates = 0;

    for (int i = 0; i < numRooms; i++) {
        roomStartIndex[i] = totalStates;
        totalStates += possibleChillingLevels[i].size();
    }

    vector<vector<Connection>> graph(totalStates);

    for (int i = 0; i < numRooms; i++) {
        int numChillLevels = possibleChillingLevels[i].size();
        int baseIdx = roomStartIndex[i];

        for (int j = 0; j < numChillLevels - 1; j++) {
            int stateA = baseIdx + j;
            int stateB = baseIdx + j + 1;
            ll costChange = possibleChillingLevels[i][j + 1] - possibleChillingLevels[i][j];

            graph[stateA].push_back({stateB, costChange});
            graph[stateB].push_back({stateA, costChange});
        }
    }

    for (auto &tunnel : tunnels) {
        int roomA = tunnel.roomA, roomB = tunnel.roomB;
        ll requiredChill = tunnel.requiredChill;

        int indexA = int(lower_bound(possibleChillingLevels[roomA].begin(), possibleChillingLevels[roomA].end(), requiredChill) - possibleChillingLevels[roomA].begin());
        int stateA = roomStartIndex[roomA] + indexA;
        int indexB = int(lower_bound(possibleChillingLevels[roomB].begin(), possibleChillingLevels[roomB].end(), requiredChill) - possibleChillingLevels[roomB].begin());
        int stateB = roomStartIndex[roomB] + indexB;

        graph[stateA].push_back({stateB, 0});
        graph[stateB].push_back({stateA, 0});
    }

    const ll INF = 1LL << 60;
    vector<ll> minCost(totalStates, INF);

    int startChillIndex = int(lower_bound(possibleChillingLevels[0].begin(), possibleChillingLevels[0].end(), 0) - possibleChillingLevels[0].begin());
    int startState = roomStartIndex[0] + startChillIndex;

    minCost[startState] = 0;
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> pq;
    pq.push({0, startState});

    while (!pq.empty()) {
        auto [currentCost, currentState] = pq.top();
        pq.pop();

        if (currentCost != minCost[currentState]) continue;

        for (auto &connection : graph[currentState]) {
            int nextState = connection.destination;
            ll newCost = currentCost + connection.cost;

            if (newCost < minCost[nextState]) {
                minCost[nextState] = newCost;
                pq.push({newCost, nextState});
            }
        }
    }

    ll result = INF;
    int finalRoomBaseIndex = roomStartIndex[numRooms - 1];
    int numFinalChillLevels = possibleChillingLevels[numRooms - 1].size();

    for (int i = 0; i < numFinalChillLevels; i++) {
        result = min(result, minCost[finalRoomBaseIndex + i]);
    }

    cout << result << endl;
}