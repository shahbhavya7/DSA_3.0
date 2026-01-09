#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    void nextPermutation(vector<int> &nums)
    {
        next_permutation(nums.begin(), nums.end());
    }
};

class SolutionOptimized
{ 
public:
    void nextPermutation(vector<int> &nums){
        int n  = nums.size();
        int index  = 1;

        for(int i=n-2;i>=0;i--){ // Find the first decreasing element from end
            if(nums[i]<nums[i+1]){
                index = i; // to capture the index of the first decreasing element
                break;
            }
        }
        for (int i = n-1; i > index; i--) {  // find the just larger element to swap with
            if(nums[i]>nums[index]){
                swap(nums[i],nums[index]);
                break;
            }
        }
        reverse(nums.begin()+index+1,nums.end()); // reverse the elements after the index to maintain the smallest order
    }

};
    int main()
    {
        Solution sol;
        vector<int> nums = {1,2,3,6,5,4};
        sol.nextPermutation(nums);
        for (int num : nums)
        {
            cout << num << " ";
        }
        SolutionOptimized solOpt;
        nums = {1,2,3,6,5,4};
        solOpt.nextPermutation(nums);
        cout << endl;
        for (int num : nums)
        {
            cout << num << " ";
        }

        return 0;
    }