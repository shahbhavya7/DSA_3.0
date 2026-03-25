#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool hasGroupsSizeX(vector<int>& deck) {
        unordered_map<int, int> count;
        for (auto card : deck) count[card]++;
        int res = 0;
        for (auto i : count) { 
            // the concept is to find the gcd of all the counts, if the gcd is greater than or equal to 2, then we can divide the deck into groups of that size
            // for example, if we have counts of 4, 4, 2, the gcd is 2, so we can divide the deck into groups of 2
            // if gcd is 1, then we cannot divide the deck into groups as we cannot have groups of size 1
            // if any count is 1, then the gcd will be 1, meaning there is at least one card that cannot be grouped with any other card, so we can return false immediately 
            res = __gcd(res, i.second);
        }
        if (res >= 2) return true;
        return false;
    }
};

int main(){
    Solution sol;
    vector<int> deck = {1, 2, 3, 4, 4, 3, 2, 1};
    cout << sol.hasGroupsSizeX(deck) << endl; // Output: 1 (true)
    return 0;
}