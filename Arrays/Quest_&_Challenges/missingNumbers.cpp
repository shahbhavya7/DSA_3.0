#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {

        int n=nums.size();
        vector<int> freq(n+1,0); // Frequency array to count occurrences

        for(int x:nums){ 
            freq[x]++; // if the number x is present, increment its count, eg if 2 is present, mark at index 2 of freq to 1
        }
        vector<int> ans;
        for(int i=1;i<=n;i++){ // Check for numbers from 1 to n
            if(freq[i]==0){
                ans.push_back(i);
            }

        }

        return ans;
    }
};

int main(){
    Solution sol;
    vector<int> nums = {4,3,2,7,8,2,3,1};
    vector<int> missingNumbers = sol.findDisappearedNumbers(nums);
    for(int num : missingNumbers){
        cout << num << " ";
    }

    return 0;
}