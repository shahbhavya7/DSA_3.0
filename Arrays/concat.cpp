#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> result = nums;
        result.insert(result.end(), nums.begin(), nums.end()); // start from end of result, insert all elements from nums
        return result;
    }
};

int main(){
    Solution sol;
    vector<int> nums = {1, 2, 3};
    vector<int> concatenated = sol.getConcatenation(nums);
    for(int num : concatenated){
        cout << num << " ";
    }
    cout << endl;
    return 0;
}