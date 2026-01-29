#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> result;
        for (int i = 0; i < n; i++) {
            result.push_back(nums[i]);
            result.push_back(nums[i + n]);
        }
        return result;
    }
};

int main(){
    Solution sol;
    vector<int> nums = {2,5,1,3,4,7};
    int n = nums.size() / 2;
    vector<int> shuffled = sol.shuffle(nums, n);
    cout << "Shuffled Array: ";
    for (int num : shuffled) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}