#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int pivotInteger(int n) {
        vector<int> prefixSum(n + 1, 0);
        for (int i = 1; i <= n; ++i) {
            prefixSum[i] = prefixSum[i - 1] + i;
        }
        for (int i = 1; i <= n; ++i) { // if the
            if (prefixSum[i - 1] == prefixSum[n] - prefixSum[i]) {
                return i; // Found the pivot integer
            }
        }
        return -1; // No pivot integer found
    }
};

int main(){
    Solution sol;
    int n = 8; // Example input
    cout << sol.pivotInteger(n) << endl; // Output: 6 (since 1+2+3+4+5 = 15 and 7+8 = 15)
    return 0;
}