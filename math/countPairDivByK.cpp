#include<bits/stdc++.h>
using namespace std;

// class Solution {
// public:
//     long long countPairs(vector<int>& nums, int k) {
//         long long ans = 0;
//         int n = nums.size();
//         int count = n - 1;
//         for (int i = 0; i < n; i++) {
//             if (nums[i] % k == 0) {
//                 ans += count;
//                 count--;
//             }
//         }      
//         return ans;
//     }
// };

class Solution {
public:
    long long countPairs(vector<int>& nums, int k) {
        long long ans = 0;
        unordered_map<int, int> gcdCount;
        
        for (int num : nums) {
            // Find what part of 'k' this number contributes
            long long curr_gcd = __gcd(num, k);
            
            // Check against all previously seen GCDs
            for (auto& p : gcdCount) {
                if ((1LL * curr_gcd * p.first) % k == 0) {
                    ans += p.second;
                }
            }
            
            // Add the current GCD to our map for future numbers
            gcdCount[curr_gcd]++;
        }
        
        return ans;
    }
};

int main(){
    Solution sol;
    vector<int> nums = {1, 2, 3, 4, 5};
    int k = 2;
    cout << sol.countPairs(nums, k) << endl; // Output: 
    return 0;
}