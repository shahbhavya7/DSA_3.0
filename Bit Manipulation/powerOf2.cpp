#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n <= 0) return false; // Power of 2 must be positive
        return (n & (n - 1)) == 0; 
    }
};
// & operator check each bit of n in binary form like if n is 16 (10000 in binary) then n-1 will be 15 (01111 in binary), so 16 & 15 will be compared
// bit by bit like 1 & 0 = 0, 0 & 1 = 0, 0 & 1 = 0, 0 & 1 = 0, and the result will be 00000 which is equal to 0, so it will return true.
// for power of 2 has property that it has only one bit set in its binary representation and when we subtract 1 from power of 2, all binary bits of new number
// are such that are reversed, so when we do bitwise AND between power of 2 and power of 2 - 1, the result will be 0 if n is a power of 2, otherwise it will 
// be non-zero.

int main(){
    Solution sol;
    int n = 16; // Example input
    cout << sol.isPowerOfTwo(n) << endl; // Output: 1 (true, since 16 is 2^4)
    return 0;
}