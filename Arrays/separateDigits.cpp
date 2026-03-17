#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> separateDigitsBrute(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans;
        for (int i = 0; i < n; i++) {
            int num = nums[i];
            vector<int> temp;
            while(num > 0){
                int digit = num % 10; 
                temp.push_back(digit);
                num /= 10; 
            }
            reverse(temp.begin(), temp.end());
            for (int digit : temp) ans.push_back(digit);
        }
        return ans;
    }
    
    vector<int> separateDigits(vector<int>& nums){
        vector<int>ans;
        int n = nums.size();
        string s;
        for (int i = 0; i < n; i++) {
            s = s + to_string(nums[i]); 
        }
        for (char c : s) {
            ans.push_back(c - '0'); // Convert char digit to int
    }
        return ans;
    }
};

int main(){
    vector<int> nums = {13, 25, 83, 77};
    Solution sol;
    vector<int> result = sol.separateDigits(nums);
    for (int digit : result) {
        cout << digit << " ";
    }
    return 0;
}