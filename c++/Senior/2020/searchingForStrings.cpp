#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_set>

using namespace std;

int main() {
   string needle;
   string haystack;

   cin >> needle;
   cin >> haystack;

   unordered_set<string> distinctPermutations;

   sort(needle.begin(), needle.end());

   do {
      if (haystack.find(needle) != string::npos) {
         distinctPermutations.insert(needle);
      }
   } while (next_permutation(needle.begin(), needle.end()));

   cout << distinctPermutations.size() << endl;
}