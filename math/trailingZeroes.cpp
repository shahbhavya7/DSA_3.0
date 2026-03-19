#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int trailingZeroes(int n) {
        int count = 0;
        
        // Keep dividing n by 5 until n becomes 0
        while (n > 0) {
            n /= 5; 
            count += n; 
        }
        
        return count;
    }
};

int main(){
    int n = 100;
    Solution sol;
    cout << sol.trailingZeroes(n) << "\n"; // Output: 24
    return 0;
}