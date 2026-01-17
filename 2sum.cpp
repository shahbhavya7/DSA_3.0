#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {-1, -1};
    }
};

class SolutionOptimized {
public: 
     vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int>mp;
        for(int i=0;i<nums.size();i++){
            int complement=target-nums[i]; // Find the complement that adds up to the target
            if(mp.find(complement)!=mp.end()){ // find searches for key in map and returns iterator to end if not found
                return {mp[complement],i}; // Return the indices of the complement and the current number
            }
            mp[nums[i]]=i; // we store index as value and number as key
        }
        return {-1,-1};
     }
};

int main(){
    Solution sol;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = sol.twoSum(nums, target);
    for(int index : result){
        cout << index << " ";
    }

    SolutionOptimized solOpt;
    vector<int> resultOpt = solOpt.twoSum(nums, target);
    cout << endl;
    for(int index : resultOpt){
        cout << index << " ";
    }
    return 0;
}