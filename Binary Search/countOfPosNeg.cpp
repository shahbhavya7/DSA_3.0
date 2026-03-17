#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maximumCount(vector<int>& nums) {
        int posCount = 0;
        int negCount = 0;
        for (int num : nums) {
            if (num > 0) {
                posCount++;
            } else if (num < 0) {
                negCount++;
            }
        }
        return max(posCount, negCount);
    }
};

int main(){
    vector<int> nums = {-2,-1,-1,1,2,3};
    Solution sol;
    cout << sol.maximumCount(nums) << "\n"; // Output: 2
    return 0;
}