#include <bits/stdc++.h>

using namespace std;

bool isPrime(int n) {
    if (n <= 1) return false;

    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }

    return true;
}

pair<int, int> findPrimesThatAddUp(int target) {
    pair<int, int> result = {0, 0};

    for (int i = 2; i <= target / 2; i++) {
        if (isPrime(i) && isPrime(target - i)) {
            result.first = i;
            result.second = target - i;
            break;
        }
    }

    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    while (n--) {
        int number;
        cin >> number;
        int sum = number * 2;
        pair<int, int> primes = findPrimesThatAddUp(sum);
        cout << primes.first << " " << primes.second << endl;
    }
}