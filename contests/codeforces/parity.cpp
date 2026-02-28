#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> makeParityAlternating(vector<int>& nums) {
        int n  = nums.size();
        vector<int> result(2);
        int minNum = INT_MAX;
        int maxNum = INT_MIN;
        if (n == 0 || n == 1) {
            result[0] = 0;
            result[1] = 0;
            return result;
        }
        for (int num : nums) {
            minNum = min(minNum, num);
            maxNum = max(maxNum, num);
        }
        int count = 0;
        for (int i = 0; i < n-1; i++) {
            if ((nums[i] % 2 == 0 && nums[i+1] % 2 == 0) || (nums[i] % 2 != 0 && nums[i+1] % 2 != 0)) {
                if (nums[i+1]==minNum){
                    nums[i+1] = nums[i+1]+1;
                    count++;
                    minNum = minNum+1;
                }
                else if (nums[i+1]==maxNum){
                    nums[i+1] = nums[i+1]-1;
                    count++;
                    maxNum = maxNum-1;
                }
                else{
                    nums[i+1] = nums[i+1]+1;
                    count++;
                }
            }
        }
        result[0] = count;
        result[1] = maxNum-minNum;
        return result;
    }
};

int main(){
    Solution sol;
    vector<int> nums = {0,2,-2};
    vector<int> result = sol.makeParityAlternating(nums);
    for (int num : result) {
        cout << num << " ";
    }
    return 0;
}