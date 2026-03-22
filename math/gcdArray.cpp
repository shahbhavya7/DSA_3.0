#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findGCD(vector<int>& nums) {
        int n = nums.size();
        int minval  = INT_MAX, maxval = INT_MIN;
        for (int i = 0; i < n; i++) {
            minval = min(minval, nums[i]); 
            maxval = max(maxval, nums[i]); 
        }
        return __gcd(minval, maxval); 
    
    }
};

int main(){
    Solution sol;
    vector<int> nums = {2,5,6,9,10};
    int result = sol.findGCD(nums);
    cout << result << endl; // print the GCD of the smallest and largest numbers in
    return 0;
}